"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from menu.views import item_list, stock_movement
from orders.views import create_qr_code, show_table


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('stock-movement/', stock_movement, name='stock_movement'),
    path('create_qr_code/<int:table_id>/', create_qr_code, name='create_qr_code'),
    path('table/<int:table_id>/', show_table, name='show_tables'),
    
]
