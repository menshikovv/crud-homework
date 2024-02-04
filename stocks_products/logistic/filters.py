class WarehouseProductFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='products__name', lookup_expr='icontains')

    class Meta:
        model = Warehouse
        fields = ['product']
class WarehouseListView(ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WarehouseProductFilter
