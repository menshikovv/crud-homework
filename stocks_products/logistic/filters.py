import django_filters
from .models import Stock

class StockFilter(django_filters.FilterSet):
    product_id = django_filters.CharFilter(field_name='positions__product__id')

    class Meta:
        model = Stock
        fields = ['product_id']
