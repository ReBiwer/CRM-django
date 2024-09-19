from django.contrib.auth.views import LoginView
from django.urls import path

app_name = 'authorization'

urlpatterns = [
    path(
        '',
        LoginView.as_view(
            template_name="authorization/login.html",
            redirect_authenticated_user=True,
        ),
        name='login'
    )
]
