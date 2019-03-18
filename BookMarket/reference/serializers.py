from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    """сериализация модели Автор"""

    class Meta:
        model = Author
        fields = (
            'name',
            'description'
        )


class GenreSerializer(serializers.ModelSerializer):
    """сериализация модели Жанр"""

    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )


class SeriesSerializer(serializers.ModelSerializer):
    """сериализация модели Серия"""

    class Meta:
        model = Series
        fields = (
            'name',
            'description'
        )


class PublisherSerializer(serializers.ModelSerializer):
    """сериализация модели Издательство"""

    class Meta:
        model = Publisher
        fields = (
            'name',
            'description'
        )


class ManufacturerSerializer(serializers.ModelSerializer):
    """сериализация модели Изгатовитель"""

    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'description'
        )


class OrderStatusSerializer(serializers.ModelSerializer):
    """сериализация модели Статус заказа"""

    class Meta:
        model = OrderStatus
        fields = (
            'name',
            'description'
        )
