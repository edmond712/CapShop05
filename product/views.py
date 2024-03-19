from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import Response, APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView
)
from .models import Color, Category, Brand, Image, Product, Storage, Poster

from .serializers import (
    StorageListSerializer,
    FavoriteCreateSerializer,
    PosterListSerializer,
    BrandListSerializer,
    StorageCreateUpdateSerializer, ProductDetailSerializer
)
from .filters import StorageFilter


# class StorageListView(APIView):
#
#     def get(self, request):
#
#         products = Storage.objects.all()
#
#         serializer = StorageListSerializer(products, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         serializer = FavoriteCreateSerializer(data=request.data, context={'request': request})
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(status.HTTP_400_BAD_REQUEST)

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

        product = Product.objects.get(pk=pk)

        serializer = ProductDetailSerializer(product)

        return Response(serializer.data)

class StorageListView(ListCreateAPIView):
    queryset = Storage.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['product__title']
    ordering_fields = ['product__price', 'product__created_date']
    filterset_class = StorageFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StorageListSerializer
        elif self.request.method == 'POST':
            return StorageCreateUpdateSerializer


class StorageDetailView(RetrieveAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class StorageCreateView(CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateUpdateSerializer


class StorageUpdateView(UpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateUpdateSerializer


class StorageDeleteView(DestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateUpdateSerializer



