from rest_framework import serializers
from .models import Color, Category, Brand, Image, Product, Storage


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file', 'is_main')


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('title', )


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)
    brands = BrandListSerializer(many=True)

    class Meta:
        model = Product
        fields = ('images', 'title', 'brands', 'price')


class StorageListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'product')





