from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CustomerForm
from .models import Customer


class CreateCustomerView(CreateView):
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customers')


class DetailCustomerView(DetailView):
    queryset = Customer.objects.select_related('ad', 'contract')
    template_name = 'customers/customers-detail.html'


class ListCustomerView(ListView):
    queryset = Customer.objects.select_related('ad', 'contract').all()
    context_object_name = 'customers'
    template_name = 'customers/customers-list.html'


class DeleteCustomerView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers')


class UpdateCustomerView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/customers-update.html'
