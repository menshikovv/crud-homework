from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

class StockFilter(filters.FilterSet):
    product_name = filters.CharFilter(field_name='product__name', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['product_name']

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StockFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
