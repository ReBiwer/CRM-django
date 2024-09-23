from django.contrib.auth.mixins import PermissionRequiredMixin


class PermissionMarketer(PermissionRequiredMixin):
    permission_required = [
        'products.add_product',
        'products.change_product',
        'products.delete_product',
        'products.view_product',
        'ads.add_ads',
        'ads.change_ads',
        'ads.delete_ads',
        'ads.view_ads',
    ]
