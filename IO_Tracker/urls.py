from django.urls import path
from . import views

urlpatterns = [
    path('', views.IO_list, name='IO_list'),
]