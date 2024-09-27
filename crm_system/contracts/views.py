from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Contract
from .forms import ContractForm


class CreateContactView(PermissionRequiredMixin, CreateView):
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:contracts')
    permission_required = ['contracts.add_contract']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailContractView(PermissionRequiredMixin, DetailView):
    queryset = Contract.objects.select_related('created_by')
    template_name = 'contracts/contracts-detail.html'
    permission_required = ['contracts.view_contract']


class ListContractView(PermissionRequiredMixin, ListView):
    queryset = Contract.objects.all()
    context_object_name = 'contracts'
    template_name = 'contracts/contracts-list.html'
    permission_required = ['contracts.view_contract']


class DeleteContractView(PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts')
    permission_required = ['contracts.delete_contract']


class UpdateContractView(PermissionRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-update.html'
    permission_required = ['contracts.change_contract']

    def form_valid(self, form):
        form.instance.created_by = self.object.created_by
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'contracts:contract_detail',
            kwargs={'pk': self.object.pk}
        )
