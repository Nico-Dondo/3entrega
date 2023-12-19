from django.urls import path
from .views import custom_login, RegistroView

urlpatterns = [
    path('', custom_login, name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
]