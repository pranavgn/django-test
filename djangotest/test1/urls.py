from django.db import router
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from test1 import views



router = routers.DefaultRouter()
router.register(r'users', views.user_detailsViewSet)
router.register(r'posts', views.postsViewSet)
router.register(r'reviews', views.reviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]