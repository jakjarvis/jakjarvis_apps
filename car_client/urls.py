from django.urls import path
from car_client import views

urlpatterns = [
    path('launcher/', views.launcher, name='launcher'),
    ]