from django.contrib.auth.views import LoginView
from django.urls import path

from .views import MyLogoutView, IndexView

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('index/', IndexView.as_view(), name='account_index'),
]
