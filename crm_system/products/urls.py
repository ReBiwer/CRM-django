from django.urls import path

from .views import DetailProductView, CreateProductView

app_name = 'products'

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='product_create')
]
