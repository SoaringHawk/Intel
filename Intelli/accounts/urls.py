from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('', home, name='home'),
]