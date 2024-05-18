from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='info'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
]
