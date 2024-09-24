from typing import TYPE_CHECKING

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager


class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    if TYPE_CHECKING:
        objects: Manager
