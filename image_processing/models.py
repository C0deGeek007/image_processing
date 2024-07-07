from django.db import models

class ImageProcessRequest(models.Model):
    request_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='pending')

class Product(models.Model):
    request = models.ForeignKey(ImageProcessRequest, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    name = models.CharField(max_length=255)
    input_image_urls = models.TextField()
    output_image_urls = models.TextField(null=True, blank=True)
