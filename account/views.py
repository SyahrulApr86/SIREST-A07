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


def register_restoran(request):
    form = RegisterFormRestoran(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'register_restoran.html', context)


def register_kurir(request):
    form = RegisterFormKurir(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'register_kurir.html', context)

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def profile_restoran(request):
    return render(request, 'profile_restoran.html')

def profile_pelanggan(request):
    return render(request, 'profile_pelanggan.html')

def profile_kurir(request):
    return render(request, 'profile_kurir.html')
