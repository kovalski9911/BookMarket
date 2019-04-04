from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('creat-order/', views.CreateOrderView.as_view(), name='create-order'),
    path('success/<int:pk>', views.SuccessOrderView.as_view(), name='success'),
    path('list-order/', views.ListOrderView.as_view(), name='list-orders'),
    path('detail-order/<int:pk>', views.DetailOrderView.as_view(), name='detail-orders'),
    path('update-order/<int:pk>', views.UpdateOrderView.as_view(), name='update-order'),
    path('delete-order/<int:pk>', views.DeleteOrderView.as_view(), name='delete-order'),

]