from django import forms
from .models import Customer
from leads.models import Lead
from contracts.models import Contract


class CustomerForm(forms.ModelForm):
    lead = forms.ModelChoiceField(queryset=Lead.objects.select_related('ad').all())
    customer_contract = forms.ModelChoiceField(queryset=Contract.objects.all())

    class Meta:
        model = Customer
        fields = ['lead', 'customer_contract']

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.first_name = self.cleaned_data['lead'].first_name
        customer.surname = self.cleaned_data['lead'].surname
        customer.last_name = self.cleaned_data['lead'].last_name
        customer.email = self.cleaned_data['lead'].email
        customer.phone = self.cleaned_data['lead'].phone
        customer.ad = self.cleaned_data['lead'].ad
        customer.contract = self.cleaned_data['customer_contract']
        if commit:
            customer.save()
        return customer
