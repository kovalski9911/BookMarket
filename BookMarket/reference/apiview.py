from rest_framework import viewsets

from .models import *
from .serializers import *


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for Authors"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for Genres"""
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class SeriesViewSet(viewsets.ModelViewSet):
    """ViewSet for Series"""
    serializer_class = SeriesSerializer
    queryset = Series.objects.all()


class PublisherViewSet(viewsets.ModelViewSet):
    """ViewSet for Publishers"""
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class ManufacturerViewSet(viewsets.ModelViewSet):
    """ViewSet for Manufacturers"""
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for Order statuses"""
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
