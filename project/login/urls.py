# login/urls.py
from django.urls import path
from .views import custom_login, RegistroView

app_name = "login"

urlpatterns = [
    path('', custom_login, name='login'),  # Ajusta esta línea para que sea consistente con la vista que deseas mostrar
    path('registro/', RegistroView.as_view(), name='registro'),
    # Otros patrones de URL que puedas tener...
]
