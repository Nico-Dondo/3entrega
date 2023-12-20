# login/views.py
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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
            return redirect('login:registro')  
        return render(request, self.template_name, {'form': form})


def custom_login(request):
    return render(request, 'login/custom_login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login:registro')
    else:
        form = UserCreationForm()

    return render(request, 'login/registro.html', {'form': form})


def registro(request):
    users = CustomUser.objects.all()
    return render(request, 'login/registro.html', {'users': users})
