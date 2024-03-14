from rest_framework.views import Response, APIView, status
from .models import Color, Category, Brand, Image, Product, Storage
from .serializers import StorageListSerializer


class StorageListView(APIView):

    def get(self, request):

        products = Storage.objects.all()

        serializer = StorageListSerializer(products, many=True)

        return Response(serializer.data)

