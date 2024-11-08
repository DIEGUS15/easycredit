from rest_framework import viewsets
from .models import ProductType, Provider, Product
from .serializers import ProductTypeSerializer, ProviderSerializer, ProductSerializer

from rest_framework.filters import OrderingFilter

# ViewSet for productType


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

# ViewSet for Provider


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['priority']

    # def get_queryset(self):
    #     return self.request.user.products.all()
