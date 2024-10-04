from django.db import models

from typing import TYPE_CHECKING
from django.db.models import Manager
from phonenumber_field.modelfields import PhoneNumberField
from ads.models import Ads


class Lead(models.Model):
    """Модель представляющая собой потенциального клиента (лида)
    пришедшего с рекламной компании"""
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(blank=True, region='RU')
    ad = models.ForeignKey(Ads, on_delete=models.SET_NULL, null=True)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f'{self.first_name} {self.surname}'
