from django.views.generic import DetailView, CreateView
from django.shortcuts import render

from .models import Product


class CreateProductView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/products-create.html'


class DetailProductView(DetailView):
    model = Product
    template_name = 'products/products-delete.html'
