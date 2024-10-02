from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product


class ListProductView(PermissionRequiredMixin, ListView):
    """Представление для отображения всех продуктов"""
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'products/products-list.html'
    permission_required = ['products.view_product']


class DetailProductView(PermissionRequiredMixin, DetailView):
    """Представление для отображения деталей продукта"""
    model = Product
    template_name = 'products/products-detail.html'
    permission_required = ['products.view_product']


class CreateProductView(PermissionRequiredMixin, CreateView):
    """Представление для создания продукта"""
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products')
    permission_required = ['products.add_product']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateProductView(PermissionRequiredMixin, UpdateView):
    """Представление для обновления продукта"""
    model = Product
    template_name = 'products/products-update.html'
    fields = 'name', 'description', 'cost'
    permission_required = ['products.change_product']

    def get_success_url(self):
        return reverse(
            'products:products_detail',
            kwargs={'pk': self.object.pk}
        )


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    """Представление для удаления продукта"""
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products')
    permission_required = ['products.delete_product']
