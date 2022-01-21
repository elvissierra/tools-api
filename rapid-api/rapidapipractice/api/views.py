from django.contrib.auth.models import Tools, Area
from rest_framework import viewsets
from .serializers import ToolsSerializer, AreaSerializer


class ToolsViewSet(viewsets.ModelViewSet):
    queryset = Tools.objects.all().order_by("-date-joined")
    serializer_class = ToolsSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
