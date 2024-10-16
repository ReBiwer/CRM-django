from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import CustomerForm
from .models import Customer


class ListCustomerView(PermissionRequiredMixin, ListView):
    """Представление для отображения всех активных клиентов"""
    queryset = Customer.objects.all()
    context_object_name = 'customers'
    template_name = 'customers/customers-list.html'
    permission_required = ['customers.view_customer']


class DetailCustomerView(PermissionRequiredMixin, DetailView):
    """Представление для отображения деталей активного клиента"""
    queryset = Customer.objects.select_related('ad', 'contract')
    template_name = 'customers/customers-detail.html'
    permission_required = ['customers.view_customer']


class CreateCustomerView(PermissionRequiredMixin, CreateView):
    """Представление для создания активного клиента"""
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customers')
    permission_required = ['customers.add_customer']


class DeleteCustomerView(PermissionRequiredMixin, DeleteView):
    """Представление для удаления активного клиента"""
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers')
    permission_required = ['customers.delete_customer']


class UpdateCustomerView(PermissionRequiredMixin, UpdateView):
    """Представление для обновления активного клиента"""
    model = Customer
    fields = '__all__'
    template_name = 'customers/customers-update.html'
    permission_required = ['customers.change_customer']

    def get_success_url(self):
        return reverse(
            'customers:customer_detail',
            kwargs={'pk': self.object.pk}
        )
