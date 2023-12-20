from django.urls import path
from .views import custom_login

app_name = 'login'

urlpatterns = [
    path('custom_login/', custom_login, name='custom_login'),
    
]
