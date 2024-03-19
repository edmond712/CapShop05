from django.db.models import F
from rest_framework.views import Response, APIView, status
from .models import Color, Category, Brand, Image, Product, Storage, Poster
from .serializers import StorageListSerializer, FavoriteCreateSerializer, PosterListSerializer, BrandListSerializer, \
    ProductDetailSerializer


class StorageListView(APIView):

    def get(self, request):

        products = Storage.objects.all()

        serializer = StorageListSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = FavoriteCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class IndexListView(APIView):

    def get(self, request):
        # requests
        posters = Poster.objects.all()
        brands = Brand.objects.all()
        products = Storage.objects.all()
        sales = Storage.objects.filter(product__discount__gt=F('product__price'))

        # serializers
        posters_serializer = PosterListSerializer(posters, many=True)
        brands_serializer = BrandListSerializer(brands, many=True)
        products_serializer = StorageListSerializer(products, many=True)
        sales_serializer = StorageListSerializer(sales, many=True)


        data = {
            'posters': posters_serializer.data,
            'brands': brands_serializer.data,
            'bestseller': products_serializer.data,
            'sales': sales_serializer.data,
        }

        return Response(data)


class ProductDetailView(APIView):

     def get(self, request, pk):

        elements = Product.objects.get(pk=pk)

        serializer = ProductDetailSerializer(elements)

        return Response(serializer.data)

