from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='info'),
    path('product/create/', cache_page(60)(ProductCreateView.as_view()), name='create'),
    path('product/update/<int:pk>/', cache_page(60)(ProductUpdateView.as_view()), name='update'),
    path('product/delete/<int:pk>/', cache_page(60)(ProductDeleteView.as_view()), name='delete')
]
