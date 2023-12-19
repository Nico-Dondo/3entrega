from django.urls import path
from .views import custom_login

urlpatterns = [
    path('', custom_login, name='login'),

]
