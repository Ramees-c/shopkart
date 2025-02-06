from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.list_products, name='product_list'),
    path('product_detail/<pk>', views.product_detail, name='product_detail')
]
