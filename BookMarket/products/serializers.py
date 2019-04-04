from rest_framework import serializers

from reference.serializers import (
    AuthorSerializer,
    GenreSerializer,
    SeriesSerializer,
    PublisherSerializer,
    ManufacturerSerializer)
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for model Book"""

    authors = AuthorSerializer(read_only=True, many=True)
    genre = GenreSerializer(read_only=True, many=True)
    series = SeriesSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('name',
                  'cover_image',
                  'price',
                  'authors',
                  'series',
                  'genre',
                  'date_of_published',
                  'numbers_of_pages',
                  'binding',
                  'pr_format',
                  'isbn',
                  'weight',
                  'age_limit',
                  'publisher',
                  'manufacturer',
                  'stock',
                  'available',
                  'rating',
                  'created',
                  'updated'
                  )
