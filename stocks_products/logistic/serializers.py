from rest_framework import serializers
from rest_framework.filters import SearchFilter
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']
        filter_backends = [SearchFilter]
        search_fields = ['title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True, write_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)

        for position_data in positions_data:
            StockProduct.objects.create(stock=stock, **position_data)

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        for position_data in positions_data:
            product = position_data.get('product')
            quantity = position_data.get('quantity')
            price = position_data.get('price')

            stock_product, created = StockProduct.objects.update_or_create(
                stock=instance, product=product,
                defaults={'quantity': quantity, 'price': price}
            )

        return instance