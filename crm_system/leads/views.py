from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from .models import Lead


class CreateLeadView(CreateView):
    model = Lead
    fields = '__all__'
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads')


class ListLeadsView(ListView):
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    template_name = 'leads/leads-list.html'


class DetailLeadView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'


class DeleteLeadView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads')


class UpdateLeadView(UpdateView):
    model = Lead
    template_name = 'leads/leads-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse(
            'leads:lead_detail',
            kwargs={'pk': self.object.pk}
        )
