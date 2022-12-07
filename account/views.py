from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import *
from utils.query import *


# Create your views here.


def show_main(request):
    print(request.COOKIES.get('role'))
    return render(request, 'main.html', {'role':request.COOKIES.get('role')})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        cursor.execute(f'select email, password from user_acc where email = \'{email}\'')
        user = cursor.fetchmany();
        if len(user) == 1 and user[0][1] == password:
            cursor.execute(f'select u.email from user_acc u, admin a where u.email = a.email and u.email = \'{email}\'')
            if (len(cursor.fetchmany()) == 1):
                response = render(request, 'dashboard_admin.html', {'role':'admin'})
                response.set_cookie('role', 'admin')
                return response

            cursor.execute(f'select u.email from user_acc u, restaurant r where u.email = r.email and u.email = \'{email}\'')
            if (len(cursor.fetchmany()) == 1):
                response = HttpResponseRedirect(reverse('account:profile_restoran'))
                response.set_cookie('role', 'restaurant')
                return response

            cursor.execute(f'select u.email from user_acc u, courier r where u.email = r.email and u.email = \'{email}\'')
            if (len(cursor.fetchmany()) == 1):
                response = HttpResponseRedirect(reverse('account:profile_kurir'))
                response.set_cookie('role', 'courier')
                return response
 
            response = HttpResponseRedirect(reverse('account:profile_pelanggan'))
            response.set_cookie('role', 'customer')
            return response
            
    context = {}
    return render(request, 'login.html', context)

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
    # context = {
    #     'role':request.COOKIES.get('role')
    # }
    print(request.COOKIES.get('role'))
    return render(request, 'profile_restoran.html')

def profile_pelanggan(request):
    return render(request, 'profile_pelanggan.html')

def profile_kurir(request):
    return render(request, 'profile_kurir.html')
