from django.shortcuts import render
from django.contrib.auth.models import Tools, Area
from rest_framework import viewsets
from .serializers import ToolsSerializer, AreaSerializer


class ToolsViewsSet(viewsets.ModelViewSet):
    query = Tools.objects.all().order_by("-date-joined")
    serializers_class = ToolsSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.bjects.all()
    serializer_class = AreaSerializer
