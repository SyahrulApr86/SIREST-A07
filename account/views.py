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
            cursor.execute(f'select * from user_acc u, admin a where u.email = a.email and u.email = \'{email}\'')
            records_admin = cursor.fetchmany()
            if (len(records_admin) == 1):
                cursor.execute(f'select u.email, u.fname, u.lname, t.adminid from transaction_actor t, user_acc u where t.email = u.email')
                # TODO: Ganti jadi fetch all
                records_actor = cursor.fetchmany()

                for i in range(len(records_actor)):
                    cursor.execute(f'select * from courier where email = \'{records_actor[i][0]}\'')
                    if len(cursor.fetchmany()) == 1:
                        records_actor[i] += ('Kurir', )
                    cursor.execute(f'select * from customer where email = \'{records_actor[i][0]}\'')
                    if len(cursor.fetchmany()) == 1:
                        records_actor[i] += ('Pelanggan', )
                    cursor.execute(f'select * from restaurant where email = \'{records_actor[i][0]}\'')
                    if len(cursor.fetchmany()) == 1:
                        records_actor[i] += ('Restoran', )
                
                print(records_actor)

                context = {
                    'role':'admin',
                    'status':'success',
                    'email':records_admin[0][0],
                    'password':records_admin[0][1],
                    'no_telp':records_admin[0][2],
                    'fname':records_admin[0][3],
                    'lname':records_admin[0][4],
                    'records_actor':records_actor,
                }
                response = render(request, 'dashboard_admin.html', context)
                response.set_cookie('role', 'admin')
                return response

            cursor.execute(f'select u.email from user_acc u, restaurant r where u.email = r.email and u.email = \'{email}\'')
            records = cursor.fetchmany()
            if (len(records) == 1):
                context = {
                    'dataRestoran': records,
                    'role' : 'restaurant'
                }
                print(context)
                response = render(request, 'dashboard_pengguna.html', context)
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
        else:   
            context = {
                'message':'Cek kembali email dan password anda!',
                'status':'error'
            }
            return render(request, 'login.html', context)

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

def profile_restoran(request, email):
    cursor.execute(f'select * from user_acc u, transaction_actor t, restaurant r where u.email = \'{email}\' and u.email = t.email and t.email = r.email')
    record = cursor.fetchall()
    context = {
        'record':record[0],
    }
    print(record[0])
    return render(request, 'profile_restoran.html', context)

def profile_pelanggan(request, email):
    cursor.execute(f'select * from user_acc u, transaction_actor t, customer c where u.email = \'{email}\' and u.email = t.email and t.email = c.email')
    record = cursor.fetchall()
    context = {
        'record':record[0],
    }
    print(record[0])
    return render(request, 'profile_pelanggan.html', context)

def profile_kurir(request, email):
    cursor.execute(f'select * from user_acc u, transaction_actor t, courier c where u.email = \'{email}\' and u.email = t.email and t.email = c.email')
    record = cursor.fetchall()
    context = {
        'record':record[0],
    }
    return render(request, 'profile_kurir.html', context)
