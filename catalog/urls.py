from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name = 'products'),
    path('product/<int:pk>/', product_info, name = 'product_info')
]