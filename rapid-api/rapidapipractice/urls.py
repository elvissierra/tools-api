from django.urls import path, include
from rest_framework import routers
from rapidapipractice.api import views


router = routers.DefaultRouter()
router.register(r"tools", views.ToolsViewSet)
router.register(r"area", views.AreaViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
