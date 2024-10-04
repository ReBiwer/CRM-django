from typing import TYPE_CHECKING
from django.db import models
from django.db.models import Manager

from products.models import Product


class Ads(models.Model):
    """Модель рекламной компании"""
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    channel = models.CharField(max_length=100)
    budget = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f'{self.name}'
