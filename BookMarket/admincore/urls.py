from django.urls import path
from .views import DashboardAdminView


urlpatterns = [
      path('dashboard/', DashboardAdminView.as_view(), name='AdminShopDashboard'),
]
