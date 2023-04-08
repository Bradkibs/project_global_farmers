from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id', 'user_product_table']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price', 'description']


class ProductDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
