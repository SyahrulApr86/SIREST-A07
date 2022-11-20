from django.shortcuts import render
from account.forms import *

# Create your views here.
def show_main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_admin(request):
    form = RegisterFormAdmin(request.POST or None)

    context = {
        'form': form
    }
    
    return render(request, 'register_admin.html', context)

def register_pelanggan(request):
    form = RegisterFormPelanggan(request.POST or None)

    context = {
        'form': form
    }
    
    return render(request, 'register_pelanggan.html', context)

