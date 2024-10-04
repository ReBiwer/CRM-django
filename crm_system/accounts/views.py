from django.contrib.auth.views import LogoutView, TemplateView
from django.urls import reverse_lazy
from products.models import Product
from ads.models import Ads
from leads.models import Lead
from customers.models import Customer

from django.contrib.auth.mixins import LoginRequiredMixin


class MyLogoutView(LogoutView):
    """Представление для выхода из учетной записи"""
    next_page = reverse_lazy('accounts:login')


class IndexView(LoginRequiredMixin, TemplateView):
    """Представление для отображения общей статистики"""
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        """Метод возвращает контекст для шаблона"""
        context = super().get_context_data(**kwargs)
        count_objects = {
            'products_count': Product.objects.count(),
            'ads_count': Ads.objects.count(),
            'leads_count': Lead.objects.count(),
            'customers_count': Customer.objects.count(),
        }
        context = {**count_objects}
        return context
