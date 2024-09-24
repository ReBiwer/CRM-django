from django.urls import path

from .views import ListContractView, CreateContactView, DetailContractView, UpdateContractView, DeleteContractView


app_name = 'contracts'

urlpatterns = [
    path('', ListContractView.as_view(), name='contracts'),
    path('create/', CreateContactView.as_view(), name='contract_create'),
    path('detail/<int:pk>/', DetailContractView.as_view(), name='contract_detail'),
    path('update/<int:pk>/', UpdateContractView.as_view(), name='contract_update'),
    path('delete/<int:pk>/', DeleteContractView.as_view(), name='contract_delete'),
]
