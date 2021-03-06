"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import (
    home,
    products,
    customer,
    create_order,
    update_order,
    delete_order,
    )

urlpatterns = [
    path('', home,name='home'),
    path('products/', products,name='products'),
    path('customer/<int:pk>', customer,name='customer'),
    path('create-order/',create_order,name='create-order'),
    path('update-order/<int:pk>',update_order,name='update-order'),
    path('delete-order/<int:pk>',delete_order,name='delete-order'),

]
