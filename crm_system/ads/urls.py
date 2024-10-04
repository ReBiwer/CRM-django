from django.urls import path

from .views import (
    ListAdsView,
    StatisticAdsView,
    CreateAdsView,
    DetailAdsView,
    UpdateAdsView,
    DeleteAdsView
)

app_name = 'ads'

urlpatterns = [
    path('', ListAdsView.as_view(), name='ads'),
    path('statistic/', StatisticAdsView.as_view(), name='ads_statistic'),
    path('create/', CreateAdsView.as_view(), name='ad_create'),
    path('detail/<int:pk>/', DetailAdsView.as_view(), name='ad_detail'),
    path('update/<int:pk>/', UpdateAdsView.as_view(), name='ad_update'),
    path('delete/<int:pk>/', DeleteAdsView.as_view(), name='ad_delete'),
]
