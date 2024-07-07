from rest_framework import serializers
from .models import ImageProcessRequest, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ImageProcessRequestSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, write_only=True)

    class Meta:
        model = ImageProcessRequest
        fields = ['request_id', 'status', 'products']
