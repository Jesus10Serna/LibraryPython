from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets
# Create your views here.


class PostList(generics.ListCreateAPIView):
    permissions_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializers_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    permissions_classes = (IsAuthorReadOnly,)
    queryset = Post.objects.all()
    serializers_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializers_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializers_class = UserSerializer

# Esto es un CRUD entero en solo 3 líneas


class PostViewSet(viewsets.ModelViewSet):
    permissions_classes = (IsAuthorReadOnly,)
    queryset = queryset = Post.objects.all()
    serializers_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializers_class = UserSerializer
