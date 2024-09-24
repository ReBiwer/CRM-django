from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

# from crm_system.permissions import PermissionManager
from .models import Contract
from .forms import ContractForm


class CreateContactView(CreateView):
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:contracts')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailContractView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'


class ListContractView(ListView):
    queryset = Contract.objects.select_related('created_by').all()
    context_object_name = 'contracts'
    template_name = 'contracts/contracts-list.html'


class DeleteContractView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts')


class UpdateContractView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts-update.html'
    fields = 'name', 'description', 'cost', 'start_date', 'end_date'

    def get_success_url(self):
        return reverse(
            'contracts:contract_detail',
            kwargs={'pk': self.object.pk}
        )
