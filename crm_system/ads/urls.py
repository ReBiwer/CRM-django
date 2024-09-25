from django.urls import path

from .views import ListAdsView, CreateAdsView

app_name = 'ads'

urlpatterns = [
    path('', ListAdsView.as_view(), name='ads'),
    path('create/', CreateAdsView.as_view(), name='ad_create'),
]
