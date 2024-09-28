from django.contrib.auth.views import LogoutView, TemplateView
from django.urls import reverse_lazy
from products.models import Product
from ads.models import Ads
from leads.models import Lead
from customers.models import Customer


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


class IndexView(TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_objects = {
            'products_count': Product.objects.count(),
            'ads_count': Ads.objects.count(),
            'leads_count': Lead.objects.count(),
            'customers_count': Customer.objects.count(),
        }
        context = {**count_objects}
        return context
