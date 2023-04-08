from django.http import Http404
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer, ProductDeleteSerializer


# Custom permission to check If the User is a Farmer
class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_type == 'FARMER'


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsFarmer]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user_product_table=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsFarmer]
    authentication_classes = [JWTAuthentication]
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404('Product not found')


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsFarmer]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user_product_table=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsFarmer]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.queryset.filter(farmer=self.request.user)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer
    permission_classes = [IsFarmer]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.queryset.filter(farmer=self.request.user)

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404('Product not found')
