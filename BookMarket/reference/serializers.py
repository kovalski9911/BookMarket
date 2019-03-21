from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for model Author"""

    class Meta:
        model = Author
        fields = (
            'name',
            'description'
        )


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for model Genre"""

    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )


class SeriesSerializer(serializers.ModelSerializer):
    """Serializer for model Series"""

    class Meta:
        model = Series
        fields = (
            'name',
            'description'
        )


class PublisherSerializer(serializers.ModelSerializer):
    """Serializer for model Publisher"""

    class Meta:
        model = Publisher
        fields = (
            'name',
            'description'
        )


class ManufacturerSerializer(serializers.ModelSerializer):
    """Serializer for model Manufacturer"""

    class Meta:
        model = Manufacturer
        fields = (
            'name',
            'description'
        )


class OrderStatusSerializer(serializers.ModelSerializer):
    """Serializer for model Order Status"""

    class Meta:
        model = OrderStatus
        fields = (
            'name',
            'description'
        )
