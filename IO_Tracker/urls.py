from django.urls import path
from . import views

urlpatterns = [
    path('', views.IO_list, name='IO_list'),
    path('io/new/', views.io_new, name='io_new'),
    path('io/<int:pk>/edit/', views.io_edit, name='io_edit'),
]