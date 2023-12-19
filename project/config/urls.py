# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import home, about, cliente, buscar_view, borrar_resultados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('cliente/', cliente, name='cliente'),
    path('buscar/', buscar_view, name='buscar'),
    path('borrar_resultados/', borrar_resultados, name='borrar_resultados'),
    path('login/', include('login.urls')),
    path('core/', include('core.urls', namespace='core')),  # Agrega esta línea para incluir la aplicación 'core'
    # Otros patrones de URL que puedas tener...
]
