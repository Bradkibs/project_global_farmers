from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['id', 'user_product_table']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'quantity', 'price', 'description']


class ProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id']
