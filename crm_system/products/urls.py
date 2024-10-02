from django.urls import path

from .views import (
    DetailProductView,
    CreateProductView,
    ListProductView,
    DeleteProductView,
    UpdateProductView
)

app_name = 'products'

urlpatterns = [
    path('', ListProductView.as_view(), name='products'),
    path('create/', CreateProductView.as_view(), name='products_create'),
    path('detail/<int:pk>/', DetailProductView.as_view(), name='products_detail'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='products_delete'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='products_update'),
]
