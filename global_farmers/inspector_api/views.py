from django.http import Http404
from rest_framework import generics, permissions
from .models import InspectorProductRelation
from .serializers import InspectorProductRelationSerializer,\
    InspectorProductRelationCreateSerializer,\
    InspectorProductRelationUpdateSerializer,\
    InspectorProductRelationDeleteSerializer


# Custom permission to check If the User is a Farmer
class IsInspector(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_type == 'Inspector' and permissions.IsAuthenticated


class InspectorProductRelationListCreateView(generics.ListCreateAPIView):
    queryset = InspectorProductRelation.objects.all()
    serializer_class = InspectorProductRelationSerializer
    permission_classes = [IsInspector]

    def perform_create(self, serializer):
        serializer.save(inspector_name=self.request.user, product_inspected=self.request.data['product_inspected'])


class InspectorProductRelationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InspectorProductRelation.objects.all()
    serializer_class = InspectorProductRelationSerializer
    permission_classes = [IsInspector]

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404('Product not found')


class InspectorProductRelationCreateView(generics.CreateAPIView):
    queryset = InspectorProductRelation.objects.all()
    serializer_class = InspectorProductRelationCreateSerializer
    permission_classes = [IsInspector]

    def perform_create(self, serializer):
        serializer.save(inspector_name=self.request.user, product_inspected=self.request.data['product_inspected'])


class InspectorProductRelationUpdateView(generics.UpdateAPIView):
    queryset = InspectorProductRelation.objects.all()
    serializer_class = InspectorProductRelationUpdateSerializer
    permission_classes = [IsInspector]

    def get_queryset(self):
        return self.queryset.filter(inspector_name=self.request.user)


class InspectorProductRelationDeleteView(generics.DestroyAPIView):
    queryset = InspectorProductRelation.objects.all()
    serializer_class = InspectorProductRelationDeleteSerializer
    permission_classes = [IsInspector]

    def get_queryset(self):
        return self.queryset.filter(inspector_name=self.request.user)

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404('Product not found')
