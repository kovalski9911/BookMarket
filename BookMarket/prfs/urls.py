"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import PrflDetailView, PrflUpdateView, PrflListView, PrflDetailForManagersView, PrflUpdateForManagersView, PrflDeleteForManagersView


app_name = 'prfls'

urlpatterns = [
    path('prfls-view', PrflDetailView.as_view(), name='prfls-view'),
    path('prfls-update', PrflUpdateView.as_view(), name='prfls-update'),

    path('prfls-list', PrflListView.as_view(), name='prfls-list'),
    path('prfls-view/<int:pk>', PrflDetailForManagersView.as_view(), name='prfls-view-for-managers'),
    path('prfls-update/<int:pk>', PrflUpdateForManagersView.as_view(), name='prfls-update-for-managers'),
    path('prfls-delete/<int:pk>', PrflDeleteForManagersView.as_view(), name='prfls-delete-for-managers'),
]