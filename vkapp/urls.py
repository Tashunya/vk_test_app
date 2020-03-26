from django.urls import path
from . import views

urlpatterns = [
    path('', views.friend_list, name='friend_list')
]
