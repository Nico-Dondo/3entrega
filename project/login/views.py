from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render



def custom_login(request):
    
    return render(request, 'login/custom_login.html')



