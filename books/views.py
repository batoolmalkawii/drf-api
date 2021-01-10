from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from .models import Book
from .serializer import BookSerializer

# Create your views here.
class BooksListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailsView(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    