from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import *
from utils.query import *
import re

# Create your views here.


def show_main(request):
    # Jika user sudah login, redirect ke halaman dashboard
    if request.COOKIES.get('role'):
        email = request.COOKIES.get('email')
        # Role Restaurant -> Dashboard Restaurant
        if request.COOKIES.get('role') == 'restaurant':
            cursor.execute(
                f'select * from user_acc u, restaurant r, transaction_actor ta, restaurant_category rc where u.email = r.email and u.email = \'{email}\' and r.email = ta.email and r.rcategory = rc.id;'
            )
            records = cursor.fetchall()

            cursor.execute(
                f'select day, starthours, endhours from restaurant r, restaurant_operating_hours roh where name = rname and branch = rbranch and email = \'{email}\''
            )
            records_hours = cursor.fetchall()

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
                'jadwal': records_hours,
                'category': records[0][22],
                'role': 'restaurant'
            }
            response = render(request, 'dashboard_pengguna.html', context)
            response.set_cookie('role', 'restaurant')
            response.set_cookie('email', records[0][0])
            response.set_cookie('rname', records[0][5])
            response.set_cookie('rbranch', records[0][6])
            response.set_cookie('adminid', records[0][20])
            print('masuk resto')
            return response

        # Role Admin -> Dashboard Admin
        elif request.COOKIES.get('role') == 'admin':
            # Query untuk mengambil data admin
            cursor.execute(
                f'select * from user_acc u, admin a where u.email = a.email and u.email = \'{email}\'')
            records_admin = cursor.fetchall()

            # Query untuk mengambil data semua user
            cursor.execute(
                f'select u.email, u.fname, u.lname, t.adminid from transaction_actor t, user_acc u where t.email = u.email')
            records_actor = cursor.fetchall()

            # Query untuk mengambil data email dari masing-masing role
            cursor.execute(
                f'select email from courier')
            list_courier = cursor.fetchall()

            cursor.execute(
                f'select email from customer')
            list_customer = cursor.fetchall()

            cursor.execute(
                f'select email from restaurant')
            list_restaurant = cursor.fetchall()

            # Penambahan kolom role untuk setiap user
            for i in range(len(records_actor)):
                if (records_actor[i][0],) in list_courier:
                    records_actor[i] += ('Kurir', )
                elif (records_actor[i][0],) in list_customer:
                    records_actor[i] += ('Pelanggan', )
                elif (records_actor[i][0],) in list_restaurant:
                    records_actor[i] += ('Restoran', )

            print(records_admin)

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

        # Role Customer -> Dashboard Customer
        elif request.COOKIES.get('role') == 'customer':
            cursor.execute(
                f'select * from user_acc u, customer c, transaction_actor ta where u.email = c.email and u.email = \'{email}\' and c.email = ta.email')
            records = cursor.fetchmany()
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
            response = render(request, 'dashboard_pengguna.html', context)
            response.set_cookie('role', 'customer')
            response.set_cookie('email', records[0][0])
            response.set_cookie('adminid', records[0][13])
            print('masuk pelanggan')
            return response

        # Role Courier -> Dashboard Courier
        elif request.COOKIES.get('role') == 'courier':
            cursor.execute(
                f'select * from user_acc u, courier c, transaction_actor ta where u.email = c.email and u.email = \'{email}\' and c.email = ta.email')
            records = cursor.fetchmany()
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
            response = render(request, 'dashboard_pengguna.html', context)
            response.set_cookie('role', 'courier')
            response.set_cookie('email', records[0][0])
            response.set_cookie('adminid', records[0][15])
            print('masuk kurir')
            return response

    # Jika tidak ada cookie role, redirect ke halaman login
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
                f'select * from user_acc u, restaurant r, transaction_actor ta, restaurant_category rc where u.email = r.email and u.email = \'{email}\' and r.email = ta.email and r.rcategory = rc.id;'
            )
            records = cursor.fetchall()

            if (len(records) == 1):
                cursor.execute(
                    f'select day, starthours, endhours from restaurant r, restaurant_operating_hours roh where name = rname and branch = rbranch and email = \'{email}\''
                )
                records_hours = cursor.fetchall()

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
                    'jadwal': records_hours,
                    'category': records[0][22],
                    'role': 'restaurant'
                }
                response = render(request, 'dashboard_pengguna.html', context)
                response.set_cookie('role', 'restaurant')
                response.set_cookie('email', records[0][0])
                response.set_cookie('rname', records[0][5])
                response.set_cookie('rbranch', records[0][6])
                response.set_cookie('adminid', records[0][20])
                print('masuk resto')
                return response

            cursor.execute(
                f'select * from user_acc u, courier c, transaction_actor ta where u.email = c.email and u.email = \'{email}\' and c.email = ta.email')
            records = cursor.fetchmany()
            if (len(records) == 1):
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
                response.set_cookie('adminid', records[0][15])
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
                response.set_cookie('adminid', records[0][13])
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
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')

        # check email is valid or not
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            form = RegisterFormAdmin(request.POST or None)
            context = {
                'form': form,
                'message': 'Email tidak valid',
            }
            return render(request, 'register_admin.html', context)

        # if data is not complete
        if not email or not password or not nama or not no_hp:
            form = RegisterFormAdmin(request.POST or None)
            context = {
                'form': form,
                'message': 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
            }
            return render(request, 'register_admin.html', context)

        # check email is already registered or not
        cursor.execute(f'select * from user_acc where email = \'{email}\'')
        records = cursor.fetchmany()
        if len(records) > 0:
            form = RegisterFormAdmin(request.POST or None)
            context = {
                'form': form,
                'message': 'Email sudah terdaftar',
            }
            return render(request, 'register_admin.html', context)

        # insert data to database
        fname = None
        lname = None
        # if name only contains one word
        if len(nama.split()) == 1:
            fname = nama
            lname = nama
        else:
            fname = nama.split()[0]
            lname = ' '.join(nama.split()[1:])

        try:
            cursor.execute(
                f'insert into user_acc values (\'{email}\', \'{password}\', \'{no_hp}\', \'{fname}\', \'{lname}\')')
            cursor.execute(f'insert into admin values (\'{email}\')')

            connection.commit()

            # set cookie and redirect to dashboard
            response = HttpResponseRedirect(reverse('account:show_main'))
            response.set_cookie('role', 'admin')
            response.set_cookie('email', email)
            return response
        except Exception as err:
            connection.rollback()
            print("Oops! An exception has occured:", err)
            print("Exception TYPE:", type(err))
            # err slice to get only error message
            err = str(err).split('CONTEXT')[0]
            form = RegisterFormAdmin(request.POST or None)
            context = {
                'form': form,
                'message': err,
            }

            return render(request, 'register_admin.html', context)

    form = RegisterFormAdmin(request.POST or None)
    context = {
        'form': form
    }

    return render(request, 'register_admin.html', context)


def register_pelanggan(request):
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        nik = request.POST.get('nik')
        nama_bank = request.POST.get('nama_bank')
        no_rekening = request.POST.get('no_rekening')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        jenis_kelamin = request.POST.get('jenis_kelamin')

        # check email is valid or not
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            form = RegisterFormPelanggan(request.POST or None)
            context = {
                'form': form,
                'message': 'Email tidak valid',
            }
            return render(request, 'register_pelanggan.html', context)

        # if data is not complete
        if not email or not password or not nama or not no_hp or not nik or not nama_bank or not no_rekening or not tanggal_lahir or not jenis_kelamin:
            form = RegisterFormPelanggan(request.POST or None)
            context = {
                'form': form,
                'message': 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
            }
            return render(request, 'register_pelanggan.html', context)

        # check email is already registered or not
        cursor.execute(f'select * from user_acc where email = \'{email}\'')
        records = cursor.fetchmany()
        if len(records) > 0:
            form = RegisterFormPelanggan(request.POST or None)
            context = {
                'form': form,
                'message': 'Email sudah terdaftar',
            }
            return render(request, 'register_pelanggan.html', context)

        # insert data to database
        fname = None
        lname = None
        # if name only contains one word
        if len(nama.split()) == 1:
            fname = nama
            lname = nama
        else:
            fname = nama.split()[0]
            lname = ' '.join(nama.split()[1:])

        try:
            cursor.execute(
                f'insert into user_acc values (\'{email}\', \'{password}\', \'{no_hp}\', \'{fname}\', \'{lname}\')')
            cursor.execute(
                f'insert into transaction_actor values (\'{email}\', \'{nik}\', \'{nama_bank}\', \'{no_rekening}\', 0, null)')
            cursor.execute(
                f'insert into customer values (\'{email}\', \'{tanggal_lahir}\', \'{jenis_kelamin}\')')

            connection.commit()

            # set cookie and redirect to dashboard
            response = HttpResponseRedirect(reverse('account:show_main'))
            response.set_cookie('role', 'customer')
            response.set_cookie('email', email)
            response.set_cookie('adminid', None)
            return response

        except Exception as err:
            connection.rollback()
            print("Oops! An exception has occured:", err)
            print("Exception TYPE:", type(err))
            form = RegisterFormPelanggan(request.POST or None)
            # err slice to get only error message
            err = str(err).split('CONTEXT')[0]
            context = {
                'form': form,
                'message': err,
            }

            return render(request, 'register_pelanggan.html', context)

    form = RegisterFormPelanggan(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'register_pelanggan.html', context)


def register_restoran(request):
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        nik = request.POST.get('nik')
        nama_bank = request.POST.get('nama_bank')
        no_rekening = request.POST.get('no_rekening')
        nama_restoran = request.POST.get('nama_restoran')
        nama_cabang = request.POST.get('cabang')
        no_hp_restoran = request.POST.get('no_hp_restoran')
        jalan = request.POST.get('jalan')
        kecamatan = request.POST.get('kecamatan')
        kota = request.POST.get('kota')
        provinsi = request.POST.get('provinsi')
        kategori = request.POST.get('kategori')

        # check email is valid or not
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            form = RegisterFormRestoran(request.POST or None)
            context = {
                'form': form,
                'message': 'Email tidak valid',
            }
            return render(request, 'register_restoran.html', context)

        # if data is not complete
        if not email or not password or not nama or not no_hp or not nik or not nama_bank or not no_rekening or not nama_restoran or not nama_cabang or not no_hp_restoran or not jalan or not kecamatan or not kota or not provinsi or not kategori:
            form = RegisterFormRestoran(request.POST or None)
            context = {
                'form': form,
                'message': 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
            }
            return render(request, 'register_restoran.html', context)

        # check email is already registered or not
        connection.commit()
        cursor.execute(f'select * from user_acc where email = \'{email}\'')
        records = cursor.fetchmany()
        if len(records) > 0:
            form = RegisterFormRestoran(request.POST or None)
            context = {
                'form': form,
                'message': 'Email sudah terdaftar',
            }
            return render(request, 'register_restoran.html', context)

        # insert data to database
        fname = None
        lname = None
        # if name only contains one word
        if len(nama.split()) == 1:
            fname = nama
            lname = nama
        else:
            fname = nama.split()[0]
            lname = ' '.join(nama.split()[1:])

        try:
            cursor.execute(
                f'insert into user_acc values (\'{email}\', \'{password}\', \'{no_hp}\', \'{fname}\', \'{lname}\')')
            cursor.execute(
                f'insert into transaction_actor values (\'{email}\', \'{nik}\', \'{nama_bank}\', \'{no_rekening}\', 0, null)')
            cursor.execute(
                f'insert into restaurant values (\'{nama_restoran}\', \'{nama_cabang}\', \'{email}\', \'{no_hp_restoran}\', \'{jalan}\', \'{kecamatan}\', \'{kota}\', \'{provinsi}\', 0, \'{kategori}\')')

            connection.commit()

            # set cookie and redirect to dashboard
            response = HttpResponseRedirect(reverse('account:show_main'))
            response.set_cookie('role', 'restaurant')
            response.set_cookie('email', email)
            response.set_cookie('adminid', None)
            return response

        except Exception as err:
            connection.rollback()
            print("Oops! An exception has occured:", err)
            print("Exception TYPE:", type(err))
            form = RegisterFormRestoran(request.POST or None)
            # err slice to get only error message
            err = str(err).split('CONTEXT')[0]
            context = {
                'form': form,
                'message': err,
            }

            return render(request, 'register_restoran.html', context)

    form = RegisterFormRestoran(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'register_restoran.html', context)


def register_kurir(request):
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        nik = request.POST.get('nik')
        nama_bank = request.POST.get('nama_bank')
        no_rekening = request.POST.get('no_rekening')
        plat_no_kendaraan = request.POST.get('plat_no_kendaraan')
        no_sim = request.POST.get('no_sim')
        jenis_kendaraan = request.POST.get('jenis_kendaraan')
        merk_kendaraan = request.POST.get('merk_kendaraan')

        # check email is valid or not
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if not re.fullmatch(regex, email):
            form = RegisterFormKurir(request.POST or None)
            context = {
                'form': form,
                'message': 'Email tidak valid',
            }
            return render(request, 'register_kurir.html', context)

        # if data is not complete
        if not email or not password or not nama or not no_hp or not nik or not nama_bank or not no_rekening or not plat_no_kendaraan or not no_sim or not jenis_kendaraan or not merk_kendaraan:
            form = RegisterFormKurir(request.POST or None)
            context = {
                'form': form,
                'message': 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
            }
            return render(request, 'register_kurir.html', context)

        # check email is already registered or not
        connection.commit()
        cursor.execute(f'select * from user_acc where email = \'{email}\'')
        records = cursor.fetchmany()
        if len(records) > 0:
            form = RegisterFormKurir(request.POST or None)
            context = {
                'form': form,
                'message': 'Email sudah terdaftar',
            }
            return render(request, 'register_kurir.html', context)

        # insert data to database
        fname = None
        lname = None
        # if name only contains one word
        if len(nama.split()) == 1:
            fname = nama
            lname = nama
        else:
            fname = nama.split()[0]
            lname = ' '.join(nama.split()[1:])

        try:
            cursor.execute(
                f'insert into user_acc values (\'{email}\', \'{password}\', \'{no_hp}\', \'{fname}\', \'{lname}\')')
            cursor.execute(
                f'insert into transaction_actor values (\'{email}\', \'{nik}\', \'{nama_bank}\', \'{no_rekening}\', 0, null)')
            cursor.execute(
                f'insert into courier values (\'{email}\', \'{plat_no_kendaraan}\', \'{no_sim}\', \'{jenis_kendaraan}\', \'{merk_kendaraan}\')')

            connection.commit()

            # set cookie and redirect to dashboard
            response = HttpResponseRedirect(reverse('account:show_main'))
            response.set_cookie('role', 'courier')
            response.set_cookie('email', email)
            response.set_cookie('adminid', None)
            return response

        except Exception as err:
            connection.rollback()
            print("Oops! An exception has occured:", err)
            print("Exception TYPE:", type(err))
            form = RegisterFormKurir(request.POST or None)
            # err slice to get only error message
            err = str(err).split('CONTEXT')[0]
            context = {
                'form': form,
                'message': err,
            }

            return render(request, 'register_kurir.html', context)

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
    cursor.execute(
        f'select day, starthours, endhours from restaurant r, restaurant_operating_hours roh where name = rname and branch = rbranch and email = \'{email}\''
    )
    records_hours = cursor.fetchall()
    cursor.execute(
        f'select * from restaurant r, restaurant_promo rp, promo where pid =id and  r.rname = rp.rname and r.rbranch = rp.rbranch and r.email = \'{email}\''
    )
    records_promo = cursor.fetchall()

    context = {
        'role': request.COOKIES.get('role'),
        'record': record[0],
        'jadwal': records_hours,
        'promo': records_promo,
    }
    print(record[0])
    return render(request, 'profile_restoran.html', context)


def profile_pelanggan(request, email):
    cursor.execute(
        f'select u.email, password, fname || \' \' || lname as name, phonenum, nik, bankname, accountno, birthdate, sex, restopay, adminid from user_acc u, transaction_actor t, customer c where u.email = \'{email}\' and u.email = t.email and t.email = c.email')
    record = cursor.fetchall()
    context = {
        'role': request.COOKIES.get('role'),
        'record': record[0],
    }
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

def verifikasi_user(request, email_user, email_admin):
    cursor.execute(
        f'update transaction_actor set adminid = \'{email_admin}\' where email = \'{email_user}\'')
    connection.commit()
    return HttpResponseRedirect(reverse('account:show_main'))
