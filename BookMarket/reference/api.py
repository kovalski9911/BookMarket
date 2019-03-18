from rest_framework import viewsets

from .serializers import *
from .models import *


class AuthorViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Автор"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Жанр"""
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class SeriesViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Серии"""
    serializer_class = SeriesSerializer
    queryset = Series.objects.all()


class PublisherViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Издательство"""
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class ManufacturerViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Изгатовитель"""
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    """вьюсет для сериализованной модели Статус заказа"""
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
