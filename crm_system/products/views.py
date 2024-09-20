from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from django.template import RequestContext

from .models import Product


class PermissionOperator(PermissionRequiredMixin):
    permission_required = [
        'products.add_product',
        'products.change_product',
        'products.delete_product',
        'products.view_product'
    ]


class CreateProductView(PermissionOperator, CreateView):
    model = Product
    fields = 'name', 'description', 'cost'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetailProductView(PermissionOperator, DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ListProductView(PermissionOperator, ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'products/products-list.html'


class DeleteProductView(PermissionOperator, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products')


class UpdateProductView(PermissionOperator, UpdateView):
    model = Product
    template_name = 'products/products-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse(
            'products:products_detail',
            kwargs={'pk': self.object.pk}
        )

