from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
# Create your views here.


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
