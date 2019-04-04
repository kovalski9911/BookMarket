from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product>/', views.AddProductCartView.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateProductCartView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteProductCartView.as_view(), name='delete'),
    path('view/', views.ListCartView.as_view(), name='view'),
]