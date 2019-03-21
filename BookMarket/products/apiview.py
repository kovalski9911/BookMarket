from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for a Book"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
