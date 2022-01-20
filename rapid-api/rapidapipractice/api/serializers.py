from django.contrib.auth.models import Tools, Area
from rest_framework import serializers
from sqlalchemy import func


class ToolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tools
        fields = ["function", "price", "area", "name"]


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ["name", "service"]
