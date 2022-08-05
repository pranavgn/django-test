from tokenize import group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from test1.serializers import user_detailsSerializer, postsSerializer, reviewSerializer

class user_detailsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_detailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class postsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = postsSerializer
    permission_classes = [permissions.IsAuthenticated]

class reviewViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = reviewSerializer
    permission_classes = [permissions.IsAuthenticated]



