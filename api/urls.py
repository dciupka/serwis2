from django.urls import path
from . import views

urlpatterns = [
    path('json/all', views.getData, name='first_endpoint'),
]