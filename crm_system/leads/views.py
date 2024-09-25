from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Lead


class CreateLeadView(PermissionRequiredMixin, CreateView):
    model = Lead
    fields = '__all__'
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads')
    permission_required = ['leads.add_lead']


class ListLeadsView(PermissionRequiredMixin, ListView):
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    template_name = 'leads/leads-list.html'
    permission_required = ['leads.view_lead']


class DetailLeadView(PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    permission_required = ['leads.view_lead']


class DeleteLeadView(PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads')
    permission_required = ['leads.delete_lead']


class UpdateLeadView(PermissionRequiredMixin, UpdateView):
    model = Lead
    template_name = 'leads/leads-update.html'
    fields = '__all__'
    permission_required = ['leads.change_lead']

    def get_success_url(self):
        return reverse(
            'leads:lead_detail',
            kwargs={'pk': self.object.pk}
        )
