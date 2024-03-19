from rest_framework import serializers
from .models import Color, Category, Brand, Image, Product, Storage, Favorite, Poster


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file', 'is_main')


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('title', 'logo')


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)
    brands = BrandListSerializer(many=True)

    class Meta:
        model = Product
        fields = ('images', 'title', 'brands', 'price', 'discount')


class StorageListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Storage
        fields = ('id', 'product')


class FavoriteCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ('user', 'product')


class PosterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poster
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        fields = ('images', 'title', 'description', 'price', 'size')

