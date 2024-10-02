from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Lead


class ListLeadsView(PermissionRequiredMixin, ListView):
    """Представление для отображения списка лидов"""
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    template_name = 'leads/leads-list.html'
    permission_required = ['leads.view_lead']


class DetailLeadView(PermissionRequiredMixin, DetailView):
    """Представление для отображения информации о лиде"""
    model = Lead
    template_name = 'leads/leads-detail.html'
    permission_required = ['leads.view_lead']


class CreateLeadView(PermissionRequiredMixin, CreateView):
    """Представление для создания лида"""
    model = Lead
    fields = '__all__'
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads')
    permission_required = ['leads.add_lead']


class DeleteLeadView(PermissionRequiredMixin, DeleteView):
    """Представление для удаления лида"""
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads')
    permission_required = ['leads.delete_lead']


class UpdateLeadView(PermissionRequiredMixin, UpdateView):
    """Представление для обновления информации о лиде"""
    model = Lead
    template_name = 'leads/leads-update.html'
    fields = '__all__'
    permission_required = ['leads.change_lead']

    def get_success_url(self):
        return reverse(
            'leads:lead_detail',
            kwargs={'pk': self.object.pk}
        )
