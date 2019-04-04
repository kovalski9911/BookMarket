from django.urls import path

from . import views


app_name = 'comments'

urlpatterns = [
    path('add', views.CommentsAdd.as_view(), name='comments_add'),
]