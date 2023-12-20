# login/urls.py

from django.urls import path
from .views import custom_login, register, registro

app_name = 'login'

urlpatterns = [
    path('custom_login/', custom_login, name='custom_login'),
    path('register/', register, name='register'),
    path('registro/', registro, name='registro'),
]
