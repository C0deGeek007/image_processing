from celery import shared_task
from PIL import Image
from .models import ImageProcessRequest, Product
from django.conf import settings
import os
from openpyxl import Workbook

def generate_excel(products):
    wb = Workbook()
    ws = wb.active
    ws.title = "Books"

    # Define headers
    headers = ['S. NO', 'Product Name', 'input image urls', "output_image_urls"]

    # Write headers in the first row
    ws.append(headers)

    for product in products:
        ws.append([product.serial_number, product.name, product.input_image_urls, product.output_image_urls])

    # Construct the file path where you want to save the Excel file
    file_path = os.path.join(settings.BASE_DIR, 'assets', 'books.xlsx')

    # Save workbook to file path
    wb.save(file_path)


@shared_task
def process_images(request_id):
    image_process_request = ImageProcessRequest.objects.get(id=request_id)
    products = Product.objects.filter(request=image_process_request)

    assets_folder = os.path.join(settings.BASE_DIR, 'assets')

    for product in products:
        input_urls = product.input_image_urls.split(',')
        output_paths = []
        
        for index, url in enumerate(input_urls):
            img = Image.open(url)
            
            output_filename = f'{product.name}__{index}.jpg'
            output_path = assets_folder+"/"+output_filename
            
            img.save(output_path, format='JPEG', quality=50)
            
            output_paths.append(output_path)

        product.output_image_urls = ','.join(output_paths)
        product.save()

    image_process_request.status = 'completed'
    image_process_request.save()

    generate_excel(products)
