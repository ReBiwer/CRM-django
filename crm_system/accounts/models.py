from django.contrib.auth.models import User
from django.db import models
from typing import TYPE_CHECKING
from django.db.models import Manager

from products.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    second_name = models.CharField(max_length=100, null=True, blank=True)

    if TYPE_CHECKING:
        objects: Manager
