from django.urls import path
from .views import (
    PrflDetailView,
    PrflUpdateView,
    PrflListView,
    PrflDetailForManagersView,
    PrflUpdateForManagersView,
    PrflDeleteForManagersView
)


app_name = 'prfls'

urlpatterns = [
    path('prfls-view', PrflDetailView.as_view(), name='prfls-view'),
    path('prfls-update', PrflUpdateView.as_view(), name='prfls-update'),

    path('prfls-list', PrflListView.as_view(), name='prfls-list'),
    path('prfls-view/<int:pk>', PrflDetailForManagersView.as_view(), name='prfls-view-for-managers'),
    path('prfls-update/<int:pk>', PrflUpdateForManagersView.as_view(), name='prfls-update-for-managers'),
    path('prfls-delete/<int:pk>', PrflDeleteForManagersView.as_view(), name='prfls-delete-for-managers'),
]