from django.db import models
from django.forms import MultiValueField, CharField, MultiWidget, TextInput

from typing import TYPE_CHECKING
from django.db.models import Manager


class PhoneWidget(MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
                   TextInput(attrs={'size': num_length, 'maxlength': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['', '']

    @staticmethod
    def format_output(rendered_widgets):
        return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


class PhoneField(MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+7' + values[0] + values[1]


class Lead(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = PhoneField(code_length=3, num_length=7)

    if TYPE_CHECKING:
        objects: Manager
