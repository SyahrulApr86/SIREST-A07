from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import *
from utils.query import *


# Create your views here.


def show_main(request):
    if request.COOKIES.get('role'):
        email = request.COOKIES.get('email')
        if request.COOKIES.get('role') == 'restaurant':
            cursor.execute(
                f'select * from user_acc u, restaurant r, transaction_actor ta, restaurant_category rc, restaurant_operating_hours ros where u.email = r.email and u.email = \'{email}\' and r.email = ta.email and r.rcategory = rc.id and r.rname = ros.name and r.rbranch = ros.branch')
            records = cursor.fetchall()
            print(records)
            context = {
                'email': records[0][0],
                'password': records[0][1],
                'notelp': records[0][2],
                'fname': records[0][3],
                'lname': records[0][4],
                'rname': records[0][5],
                'rbranch': records[0][6],
                'rphonenum': records[0][8],
                'rstreet': records[0][9],
                'rdistrict': records[0][10],
                'rcity': records[0][11],
                'rprovince': records[0][12],
                'rating': records[0][13],
                'nik': records[0][16],
                'bank': records[0][17],
                'accountno': records[0][18],
                'restopay': records[0][19],
                'adminid': records[0][20],
                'day': records[0][25],
                'starthour': records[0][26],
                'endhour': records[0][27],
                'category': records[0][22],
                'role': 'restaurant'
            }

            response = render(request, 'dashboard_pengguna.html', context)
            response.set_cookie('role', 'restaurant')
            response.set_cookie('email', records[0][0])
            response.set_cookie('rname', records[0][5])
            response.set_cookie('rbranch', records[0][6])
            print('masuk resto')
            return response

        elif request.COOKIES.get('role') == 'admin':
            cursor.execute(
                f'select * from user_acc u, admin a where u.email = a.email and u.email = \'{email}\'')
            records_admin = cursor.fetchall()
            cursor.execute(
                f'select u.email, u.fname, u.lname, t.adminid from transaction_actor t, user_acc u where t.email = u.email')
            records_actor = cursor.fetchall()

            cursor.execute(
                f'select email from courier')
            list_courier = cursor.fetchall()

            cursor.execute(
                f'select email from customer')
            list_customer = cursor.fetchall()

            cursor.execute(
                f'select email from restaurant')
            list_restaurant = cursor.fetchall()

            for i in range(len(records_actor)):
                if (records_actor[i][0],) in list_courier:
                    records_actor[i] += ('Kurir', )
                elif (records_actor[i][0],) in list_customer:
                    records_actor[i] += ('Pelanggan', )
                elif (records_actor[i][0],) in list_restaurant:
                    records_actor[i] += ('Restoran', )

            context = {
                'role': 'admin',
                'status': 'success',
                'email': records_admin[0][0],
                'password': records_admin[0][1],
                'no_telp': records_admin[0][2],
                'fname': records_admin[0][3],
                'lname': records_admin[0][4],
                'records_actor': records_actor,
            }
            response = render(request, 'dashboard_admin.html', context)
            response.set_cookie('role', 'admin')
            response.set_cookie('email', records_admin[0][0])

            print('masuk admin')
            return response

    return render(request, 'main.html')


def logout_user(request):
    response = HttpResponseRedirect(reverse('account:show_main'))
    response.delete_cookie('email')
    response.delete_cookie('role')
    return response


def login(request):
    # if user is logged in, redirect to dashboard
    if request.COOKIES.get('role'):
        return HttpResponseRedirect(reverse('account:show_main'))

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        cursor.execute(
            f'select email, password from user_acc where email = \'{email}\'')
        user = cursor.fetchmany()
        if len(user) == 1 and user[0][1] == password:
            cursor.execute(
                f'select * from user_acc u, admin a where u.email = a.email and u.email = \'{email}\'')
            records_admin = cursor.fetchall()
            if (len(records_admin) == 1):
                cursor.execute(
                    f'select u.email, u.fname, u.lname, t.adminid from transaction_actor t, user_acc u where t.email = u.email')
                records_actor = cursor.fetchall()

                cursor.execute(
                    f'select email from courier')
                list_courier = cursor.fetchall()

                cursor.execute(
                    f'select email from customer')
                list_customer = cursor.fetchall()

                cursor.execute(
                    f'select email from restaurant')
                list_restaurant = cursor.fetchall()

                for i in range(len(records_actor)):
                    if (records_actor[i][0],) in list_courier:
                        records_actor[i] += ('Kurir', )
                    elif (records_actor[i][0],) in list_customer:
                        records_actor[i] += ('Pelanggan', )
                    elif (records_actor[i][0],) in list_restaurant:
                        records_actor[i] += ('Restoran', )

                context = {
                    'role': 'admin',
                    'status': 'success',
                    'email': records_admin[0][0],
                    'password': records_admin[0][1],
                    'no_telp': records_admin[0][2],
                    'fname': records_admin[0][3],
                    'lname': records_admin[0][4],
                    'records_actor': records_actor,
                }
                response = render(request, 'dashboard_admin.html', context)
                response.set_cookie('role', 'admin')
                response.set_cookie('email', records_admin[0][0])

                print('masuk admin')
                return response

            cursor.execute(
                f'select * from user_acc u, restaurant r, transaction_actor ta, restaurant_category rc, restaurant_operating_hours ros where u.email = r.email and u.email = \'{email}\' and r.email = ta.email and r.rcategory = rc.id and r.rname = ros.name and r.rbranch = ros.branch')
            records = cursor.fetchmany()

            if (len(records) == 1):
                # print(records)
                context = {
                    'email': records[0][0],
                    'password': records[0][1],
                    'notelp': records[0][2],
                    'fname': records[0][3],
                    'lname': records[0][4],
                    'rname': records[0][5],
                    'rbranch': records[0][6],
                    'rphonenum': records[0][8],
                    'rstreet': records[0][9],
                    'rdistrict': records[0][10],
                    'rcity': records[0][11],
                    'rprovince': records[0][12],
                    'rating': records[0][13],
                    'nik': records[0][16],
                    'bank': records[0][17],
                    'accountno': records[0][18],
                    'restopay': records[0][19],
                    'adminid': records[0][20],
                    'day': records[0][25],
                    'starthour': records[0][26],
                    'endhour': records[0][27],
                    'category': records[0][22],
                    'role': 'restaurant'
                }
                # print(context)
                response = render(request, 'dashboard_pengguna.html', context)
                response.set_cookie('role', 'restaurant')
                response.set_cookie('email', records[0][0])
                print(email)
                response.set_cookie('rname', records[0][5])
                response.set_cookie('rbranch', records[0][6])
                print('masuk resto')
                return response

            cursor.execute(
                f'select * from user_acc u, courier c, transaction_actor ta where u.email = c.email and u.email = \'{email}\' and c.email = ta.email')
            records = cursor.fetchmany()
            if (len(records) == 1):
                # response = render(request, 'dashboard_admin.html', {'role':'admin', 'status':'success'})
                # print(records)
                context = {
                    'email': records[0][0],
                    'password': records[0][1],
                    'notelp': records[0][2],
                    'fname': records[0][3],
                    'lname': records[0][4],
                    'plat': records[0][6],
                    'nosim': records[0][7],
                    'vehicletype': records[0][8],
                    'vehiclebrand': records[0][9],
                    'nik': records[0][11],
                    'bank': records[0][12],
                    'accountno': records[0][13],
                    'restopay': records[0][14],
                    'adminid': records[0][15],
                    'role': 'courier'
                }
                # print(context)
                response = render(request, 'dashboard_pengguna.html', context)
                response.set_cookie('role', 'courier')
                response.set_cookie('email', records[0][0])
                print('masuk kurir')
                return response

            cursor.execute(
                f'select * from user_acc u, customer c, transaction_actor ta where u.email = c.email and u.email = \'{email}\' and c.email = ta.email')
            records = cursor.fetchmany()
            if (len(records) == 1):
                # print(records)
                context = {
                    'email': records[0][0],
                    'password': records[0][1],
                    'notelp': records[0][2],
                    'fname': records[0][3],
                    'lname': records[0][4],
                    'tanggallahir': records[0][6],
                    'gender': records[0][7],
                    'nik': records[0][9],
                    'bank': records[0][10],
                    'accountno': records[0][11],
                    'restopay': records[0][12],
                    'adminid': records[0][13],
                    'role': 'customer'
                }
                # print(context)
                response = render(request, 'dashboard_pengguna.html', context)
                response.set_cookie('role', 'customer')
                response.set_cookie('email', records[0][0])
                print('masuk pelanggan')
                return response

            # response = HttpResponseRedirect(reverse('account:profile_pelanggan'))
            # response.set_cookie('role', 'customer')
            # return response
        else:
            context = {
                'message': 'Cek kembali email dan password anda!',
                'status': 'error',
                'role': None,
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
    cursor.execute(
        f'select * from user_acc u, transaction_actor t, restaurant r where u.email = \'{email}\' and u.email = t.email and t.email = r.email')
    record = cursor.fetchall()
    context = {
        'role': request.COOKIES.get('role'),
        'record': record[0],
    }
    print(record[0])
    return render(request, 'profile_restoran.html', context)


def profile_pelanggan(request, email):
    cursor.execute(
        f'select * from user_acc u, transaction_actor t, customer c where u.email = \'{email}\' and u.email = t.email and t.email = c.email')
    record = cursor.fetchall()
    context = {
        'role': request.COOKIES.get('role'),
        'record': record[0],
    }
    print(record[0])
    return render(request, 'profile_pelanggan.html', context)


def profile_kurir(request, email):
    cursor.execute(
        f'select * from user_acc u, transaction_actor t, courier c where u.email = \'{email}\' and u.email = t.email and t.email = c.email')
    record = cursor.fetchall()
    context = {
        'role': request.COOKIES.get('role'),
        'record': record[0],
    }
    return render(request, 'profile_kurir.html', context)
