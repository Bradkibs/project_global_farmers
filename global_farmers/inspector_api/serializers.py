from .models import InspectorProductRelation
from rest_framework import serializers


class InspectorProductRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorProductRelation
        field = '__all__'


class InspectorProductRelationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorProductRelation
        exclude = ['id', 'inspector_name']


class InspectorProductRelationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorProductRelation
        field = ['comments', 'grade', 'status', 'restriction']


class InspectorProductRelationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorProductRelation
        field = ['id']
