"""jakjarvis URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from stock import views, ticker

urlpatterns = [

    # View stocks
    path('home/', views.home, name='stockhome'),
    path('create/', views.createstock, name='createstock'),
    path('current/', views.currentstocks, name='currentstocks'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('stocks/<int:stock_pk>', views.viewstock, name='viewstock'),
    path('stocks/<int:stock_pk>/delete', views.deletestock, name='deletestock'),
    path('overview/', views.overview, name='overview'),

    # Plotly-dash
    path('django_plotly_dash/', include('django_plotly_dash.urls')),

]