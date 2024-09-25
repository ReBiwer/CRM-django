from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product


class CreateProductView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products')
    permission_required = ['products.add_product']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailProductView(PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    permission_required = ['products.view_product']


class ListProductView(PermissionRequiredMixin, ListView):
    queryset = Product.objects.select_related('created_by').all()
    context_object_name = 'products'
    template_name = 'products/products-list.html'
    permission_required = ['products.view_product']


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products')
    permission_required = ['products.delete_product']


class UpdateProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/products-update.html'
    fields = 'name', 'description', 'cost'
    permission_required = ['products.change_product']

    def get_success_url(self):
        return reverse(
            'products:products_detail',
            kwargs={'pk': self.object.pk}
        )

