from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CustomerForm
from .models import Customer


class CreateCustomerView(PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customers')
    permission_required = ['customers.add_customer']


class DetailCustomerView(PermissionRequiredMixin, DetailView):
    queryset = Customer.objects.select_related('ad', 'contract')
    template_name = 'customers/customers-detail.html'
    permission_required = ['customers.view_customer']


class ListCustomerView(PermissionRequiredMixin, ListView):
    queryset = Customer.objects.all()
    context_object_name = 'customers'
    template_name = 'customers/customers-list.html'
    permission_required = ['customers.view_customer']


class DeleteCustomerView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers')
    permission_required = ['customers.delete_customer']


class UpdateCustomerView(PermissionRequiredMixin, UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/customers-update.html'
    permission_required = ['customers.change_customer']
