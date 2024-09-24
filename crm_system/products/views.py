from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from crm_system.permissions import PermissionMarketer
from .models import Product


class CreateProductView(PermissionMarketer, CreateView):
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailProductView(PermissionMarketer, DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ListProductView(PermissionMarketer, ListView):
    queryset = Product.objects.select_related('created_by').all()
    context_object_name = 'products'
    template_name = 'products/products-list.html'


class DeleteProductView(PermissionMarketer, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products')


class UpdateProductView(PermissionMarketer, UpdateView):
    model = Product
    template_name = 'products/products-update.html'
    fields = 'name', 'description', 'cost'

    def get_success_url(self):
        return reverse(
            'products:products_detail',
            kwargs={'pk': self.object.pk}
        )

