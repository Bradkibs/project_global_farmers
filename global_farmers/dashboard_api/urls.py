from django.urls import path
from .views import DashboardFarmerView, \
                    DashboardInspectorView, \
                    DashboardBuyerView

urlpatterns = [
    path('i/<uuid:pk>', DashboardInspectorView.as_view(), name='dashboard-inspector-view'),
    path('f/<uuid:pk>', DashboardFarmerView.as_view(), name='dashboard-farmer-view'),
    path('b/<uuid:pk>', DashboardBuyerView.as_view(), name='dashboard-buyer-view'),
    ]
