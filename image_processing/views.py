from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageProcessRequest, Product
from .serializers import ImageProcessRequestSerializer
from .tasks import process_images
import uuid
from django.conf import settings
import os
import pandas as pd

ASSETS_FOLDER = os.path.join(settings.BASE_DIR, 'assets')

class UploadCSV(APIView):
    def post(self, request):

        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=400)

        excel_file = request.FILES['file']
        try:
            df = pd.read_excel(excel_file)
            data = df.to_dict(orient='records')
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
        request_id = str(uuid.uuid4())
        image_process_request = ImageProcessRequest.objects.create(request_id=request_id)
        
        products_data = []

        for sku in data:
            image_string = sku.get('input_image_urls')
            image_list = image_string.split(',')
            modified_image_list = [f"{ASSETS_FOLDER}{img}" for img in image_list]
            modified_image_string = ','.join(modified_image_list)
            sku['input_image_urls'] = modified_image_string
            sku['request'] = image_process_request
            products_data.append(sku)

        for product_data in products_data:
            Product.objects.create(**product_data)

        process_images.delay(image_process_request.id)

        return Response({'request_id': request_id}, status=status.HTTP_201_CREATED)

class CheckStatus(APIView):
    def get(self, request, request_id):
        image_process_request = get_object_or_404(ImageProcessRequest, request_id=request_id)
        serializer = ImageProcessRequestSerializer(image_process_request)
        return Response(serializer.data)
