from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=['%d.%m.%Y'], widget=forms.DateInput(format='%d.%m.%Y'))
    end_date = forms.DateField(input_formats=['%d.%m.%Y'], widget=forms.DateInput(format='%d.%m.%Y'))

    class Meta:
        model = Contract
        fields = [
            'name',
            'product',
            'document',
            'description',
            'cost',
            'start_date',
            'end_date',
        ]
