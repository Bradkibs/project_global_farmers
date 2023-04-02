from django.urls import path
from .views import InspectorProductRelationCreateView,\
    InspectorProductRelationListCreateView, \
    InspectorProductRelationDetailView, \
    InspectorProductRelationUpdateView, \
    InspectorProductRelationDeleteView

urlpatterns = [
    path('create/', InspectorProductRelationCreateView.as_view(), name='inspector_product_relation-create'),
    path('', InspectorProductRelationListCreateView.as_view(), name='inspector_product_relation_list-create'),
    path('<uuid:pk>/', InspectorProductRelationDetailView.as_view(), name='inspector_product_relation-detail'),
    path('<uuid:pk>/update/', InspectorProductRelationUpdateView.as_view(), name='inspector_product_relation-update'),
    path('<uuid:pk>/delete/', InspectorProductRelationDeleteView.as_view(), name='inspector_product_relation-delete'),
]
