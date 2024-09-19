from django.urls import path

from .views import DetailProductView, CreateProductView, ListProductView

app_name = 'products'

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='products_create'),
    path('list/', ListProductView.as_view(), name='products_list'),
    path('detail/<int:pk>/', DetailProductView.as_view(), name='products_detail'),
]
