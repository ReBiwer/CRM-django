from django.urls import path

from .views import ListLeadsView, CreateLeadView

app_name = 'leads'

urlpatterns = [
    path('', ListLeadsView.as_view(), name='leads_list'),
    path('create/', CreateLeadView.as_view(), name='lead_create'),
]
