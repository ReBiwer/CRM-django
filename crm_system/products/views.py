from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

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
