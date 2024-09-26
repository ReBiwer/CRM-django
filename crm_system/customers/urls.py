from django.urls import path

from .views import ListCustomerView, CreateCustomerView, DetailCustomerView, UpdateCustomerView, DeleteCustomerView


app_name = 'customers'

urlpatterns = [
    path('', ListCustomerView.as_view(), name='customers'),
    path('create/', CreateCustomerView.as_view(), name='customer_create'),
    path('detail/<int:pk>/', DetailCustomerView.as_view(), name='customer_detail'),
    path('update/<int:pk>/', UpdateCustomerView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', DeleteCustomerView.as_view(), name='customer_delete'),
]
