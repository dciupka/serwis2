from django.urls import path
from . import views

app_name = 'serwis2'

urlpatterns = [
    path('', views.index, name='index'),
    path('endpoint/', views.endpoint, name='endpoint'),
]