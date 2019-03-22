from django.urls import path
from .views import (
    PrflDetailView,
    PrflUpdateView,
    PrflListView,
    PrflDetailForManagersView,
    PrflUpdateForManagersView,
    PrflDeleteForManagersView
)

from .apiview import (
    users_list_api_view,
    register_user_api_view,
    login_user_api_view,
    users_update_api_view,
)


app_name = 'prfls'

urlpatterns = [
    # api
    path('api-users-list', users_list_api_view, name='api-users-list'),
    path('api-users-update/<int:pk>', users_update_api_view, name='api-users-update'),

    path('api-user-register', register_user_api_view, name='api-user-register'),
    path('api-user-login', login_user_api_view, name='api-user-login'),


    # base
    path('prfls-view', PrflDetailView.as_view(), name='prfls-view'),
    path('prfls-update', PrflUpdateView.as_view(), name='prfls-update'),

    path('prfls-list', PrflListView.as_view(), name='prfls-list'),
    path('prfls-view/<int:pk>', PrflDetailForManagersView.as_view(), name='prfls-view-for-managers'),
    path('prfls-update/<int:pk>', PrflUpdateForManagersView.as_view(), name='prfls-update-for-managers'),
    path('prfls-delete/<int:pk>', PrflDeleteForManagersView.as_view(), name='prfls-delete-for-managers'),
]