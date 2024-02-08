from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
