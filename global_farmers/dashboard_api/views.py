from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from .serializers import DashboardProductSerializer
from product_api.models import Product
from product_api.views import ProductListCreateView, \
                                ProductDetailView, \
                                ProductCreateView, \
                                ProductUpdateView, \
                                ProductDeleteView
from inspector_api.views import InspectorProductRelationListCreateView, \
                                InspectorProductRelationDetailView, \
                                InspectorProductRelationCreateView, \
                                InspectorProductRelationUpdateView, \
                                InspectorProductRelationDeleteView


class DashboardFarmerView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'FARMER':
            views = {
                'product_list_create_view': ProductListCreateView.as_view()(request).data,
                'product_detail_view': ProductDetailView.as_view()(request).data,
                'product_create_view': ProductCreateView.as_view()(request).data,
                'product_update_view': ProductUpdateView.as_view()(request).data,
                'product_delete_view': ProductDeleteView.as_view()(request).data,
            }
            return JsonResponse(views)
        else:
            return JsonResponse({'error': 'You are not authorized to view this page'}, status=status.HTTP_401_UNAUTHORIZED)


class DashboardInspectorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'INSPECTOR':
            views = {
                'inspector_product_relation_list_create_view': InspectorProductRelationListCreateView.as_view()(request).data,
                'inspector_product_relation_detail_view': InspectorProductRelationDetailView.as_view()(request).data,
                'inspector_product_relation_create_view': InspectorProductRelationCreateView.as_view()(request).data,
                'inspector_product_relation_update_view': InspectorProductRelationUpdateView.as_view()(request).data,
                'inspector_product_relation_delete_view': InspectorProductRelationDeleteView.as_view()(request).data,
            }
            return JsonResponse(views)
        else:
            return JsonResponse({'error': 'You are not authorized to view this page'}, status=status.HTTP_401_UNAUTHORIZED)


class DashboardBuyerView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == 'BUYER':
            products = Product.objects.all()
            serializer = DashboardProductSerializer(products, many=True)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'error': 'You are not authorized to view this page'}, status=status.HTTP_401_UNAUTHORIZED)