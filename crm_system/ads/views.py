from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Ads


class CreateAdsView(CreateView):
    queryset = Ads.objects.select_related('product').all()
    fields = '__all__'
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads')


class DetailAdsView(DetailView):
    queryset = Ads.objects.select_related('product').all()
    template_name = 'ads/ads-detail.html'


class ListAdsView(ListView):
    queryset = Ads.objects.all()
    context_object_name = 'ads'
    template_name = 'ads/ads-list.html'


class DeleteAdsView(DeleteView):
    model = Ads
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads')


class UpdateAdsView(UpdateView):
    model = Ads
    template_name = 'ads/ads-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse(
            'ads:ad_detail',
            kwargs={'pk': self.object.pk}
        )
