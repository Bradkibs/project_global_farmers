from rest_framework import serializers
from product_api.models import Product


class DashboardProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
