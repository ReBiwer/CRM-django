from django.views.generic import DetailView
from django.shortcuts import render

from .models import Product


class DetailProductView(DetailView):
    model = Product
