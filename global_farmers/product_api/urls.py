from django.urls import path
from .views import ProductCreateView, \
    ProductListCreateView, \
    ProductDetailView, \
    ProductUpdateView,\
    ProductDeleteView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<uuid:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<uuid:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
