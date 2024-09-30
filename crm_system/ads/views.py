from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView, TemplateView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Ads
from functools import reduce
from decimal import Decimal
from leads.models import Lead
from customers.models import Customer


class ListAdsView(PermissionRequiredMixin, ListView):
    queryset = Ads.objects.all()
    context_object_name = 'ads'
    template_name = 'ads/ads-list.html'
    permission_required = ['ads.view_ads']


class CreateAdsView(PermissionRequiredMixin, CreateView):
    queryset = Ads.objects.select_related('product').all()
    fields = '__all__'
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads')
    permission_required = ['ads.add_ads']


class DetailAdsView(PermissionRequiredMixin, DetailView):
    queryset = Ads.objects.select_related('product').all()
    template_name = 'ads/ads-detail.html'
    permission_required = ['ads.view_ads']


class DeleteAdsView(PermissionRequiredMixin, DeleteView):
    model = Ads
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads')
    permission_required = ['ads.delete_ads']


class UpdateAdsView(PermissionRequiredMixin, UpdateView):
    model = Ads
    template_name = 'ads/ads-update.html'
    fields = '__all__'
    permission_required = ['ads.change_ads']

    def get_success_url(self):
        return reverse(
            'ads:ad_detail',
            kwargs={'pk': self.object.pk}
        )


class StatisticAdsView(TemplateView):
    template_name = 'ads/ads-statistic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_statistic = list()
        for ad in Ads.objects.all():
            sum_cost_contracts = 0
            for customer in Customer.objects.filter(ad=ad.pk):
                sum_cost_contracts += customer.contract.cost
            list_statistic.append(
                (
                    ad,
                    Lead.objects.filter(ad=ad.pk).count(),
                    Customer.objects.filter(ad=ad.pk).count(),
                    sum_cost_contracts / ad.budget,
                )
            )
        context['statistic'] = list_statistic
        return context

