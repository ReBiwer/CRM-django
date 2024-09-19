from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from .models import Product


class CreateProductView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products_list')


class DetailProductView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ListProductView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'products/products-list.html'


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products_list')


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'products/products-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse(
            'products:products_detail',
            kwargs={'pk': self.object.pk}
        )

