from typing import TYPE_CHECKING

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager


class Product(models.Model):
    """Модель представляющая услугу
    name: название услуги
    description: описание услуги
    cost: стоимость услуги
    created_by: кто создал эту услугу
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f'{self.name} цена {self.cost}'
