from django.urls import path

from .views import ListLeadsView, CreateLeadView, DetailLeadView, DeleteLeadView, UpdateLeadView

app_name = 'leads'

urlpatterns = [
    path('', ListLeadsView.as_view(), name='leads'),
    path('create/', CreateLeadView.as_view(), name='lead_create'),
    path('detail/<int:pk>/', DetailLeadView.as_view(), name='lead_detail'),
    path('delete/<int:pk>/', DeleteLeadView.as_view(), name='lead_delete'),
    path('update/<int:pk>/', UpdateLeadView.as_view(), name='lead_update'),
]
