from django.urls import path
from rest_framework import routers

from products.views import (
    BookProdListView,
    BookProdCreateView,
    BookProdDetailView,
    BookProdUpdateView,
    BookProdDeleteView,
)
from .apiview import BookViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register('books', BookViewSet, 'api-books')

urlpatterns = [
    # url авторов
    path('book-prod-list/', BookProdListView.as_view(), name='book-prod-list'),
    path('book-prod-create/', BookProdCreateView.as_view(), name='book-prod-create'),
    path('book-prod-view/<int:pk>/', BookProdDetailView.as_view(), name='book-prod-view'),
    path('book-prod-update/<int:pk>/', BookProdUpdateView.as_view(), name='book-prod-update'),
    path('book-prod-delete/<int:pk>/', BookProdDeleteView.as_view(), name='book-prod-delete'),
]

urlpatterns += router.urls
