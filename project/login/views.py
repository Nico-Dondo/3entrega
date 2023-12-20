# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views import View
from django.contrib import messages

class RegistroView(View):
    template_name = 'login/registro.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuario registrado con éxito. Por favor, inicia sesión.')
            return redirect('login')  
        return render(request, self.template_name, {'form': form})


def custom_login(request):
    # Tu lógica de vista aquí
    return render(request, 'login/custom_login.html')
