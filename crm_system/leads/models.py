from django.db import models

from typing import TYPE_CHECKING
from django.db.models import Manager
from phonenumber_field.modelfields import PhoneNumberField


class Lead(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = PhoneNumberField(blank=True, region='RU')

    if TYPE_CHECKING:
        objects: Manager
