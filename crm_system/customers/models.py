from django.db import models

from typing import TYPE_CHECKING
from django.db.models import Manager
from phonenumber_field.modelfields import PhoneNumberField
from ads.models import Ads
from contracts.models import Contract


class Customer(models.Model):
    """
    Модель представляющая активного клиента
    first_name: имя
    surname: фамилия
    last_name: отчество
    email: электронная почта
    phone: номер телефона
    ad: рекламная компания откуда пришел клиент
    contract: контракт с клиентом
    """
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(blank=True, region='RU')
    ad = models.ForeignKey(Ads, on_delete=models.SET_NULL, null=True)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)

    if TYPE_CHECKING:
        objects: Manager

    def __str__(self):
        return f'{self.first_name} {self.surname}'
