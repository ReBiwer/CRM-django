from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Manager


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    if TYPE_CHECKING:
        objects: Manager
