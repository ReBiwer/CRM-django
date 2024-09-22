from django.db import models

from products.models import Product


class Ads(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    channel = models.CharField(max_length=100)
    budget = models.DecimalField(default=0, max_digits=8, decimal_places=2)
