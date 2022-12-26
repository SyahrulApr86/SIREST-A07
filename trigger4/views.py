from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from utils.query import *
from trigger4.forms import *

# Create your views here.


def show_detail_riwayat(request, email, datetime):
    # query riwayat by id
    sql = f'''select u.fname, u.lname, t.street, t.district, t.city, t.province, r.rname, r.rbranch, t.datetime, t.rating, foo.fname, foo.lname, co.platenum, co.vehicletype, co.vehiclebrand, 
    r.street, r.district, r.city, r.province, t.totalfood, t.totaldiscount, t.deliveryfee, t.totalprice, pm.name, ps.name from transaction t, courier co, transaction_food tf,  
    customer cu, restaurant r, user_acc u, (select ua.email, ua.fname, ua.lname from user_acc ua) as foo, payment_method pm, payment_status ps where t.courierid = co.email and t.email = cu.email and t.email = u.email and co.email
      = foo.email and pm.id = t.pmid and ps.id = t.psid and t.email = \'{email}\' and t.datetime = \'{datetime}\' and (r.rname, r.rbranch) = (tf.rname, tf.rbranch) and (t.email, t.datetime) = (tf.email, tf.datetime);
    '''
    cursor.execute(sql)
    record_riwayat = cursor.fetchall()

    cursor.execute(
        f'select tf.foodname, tf.note, tf.amount from transaction_food tf where tf.email = \'{email}\' and tf.datetime = \'{datetime}\';')
    ordered_food = cursor.fetchall()
    cursor.execute(
        f'select ts.name, th.datetimestatus from transaction_status ts, transaction_history th where ts.id = th.tsid and th.email = \'{email}\' and th.datetime = \'{datetime}\'')
    transaction_status = cursor.fetchall()

    for i in range(len(transaction_status)):
        transaction_status[i] = list(transaction_status[i])
        transaction_status[i][1] = transaction_status[i][1].strftime(
            "%m/%d/%Y %H:%M:%S")

    context = {
        'record_riwayat': record_riwayat,
        'ordered_food': ordered_food,
        'transaction_status': transaction_status,
        'status': transaction_status[-1][0],
        'role': request.COOKIES.get('role'),
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
    }
    print('masuk')
    print(record_riwayat)
    print(ordered_food)
    print(transaction_status)
    return render(request, 'konfiirmasi_pembayaran.html', context)


def pesanan_berlangsung(request):
    context = {
        'pesanan_berlangsung': [
            {
                'restoran': 'Sego Berkat',
                'waktu_pesanan_dibuat': '2022-11-04 11:30:05',
                'status_pesanan': 'Menunggu Konfirmasi Restoran',

            },
            {
                'restoran': 'Sego sami',
                'waktu_pesanan_dibuat': '2022-11-06 11:30:05',
                'status_pesanan': 'Menunggu Konfirmasi Restoran',

            },
        ]
    }
    return render(request, 'pesanan_berlangsung.html', context)


def ringkasan_pesanan(request):
    context = {
        'nama': 'Budi',
        'waktu_pemesanan': '2020-01-01 00:00:00',
        'status_pesanan': 'Pesanan Dibuat',
        'jalan': 'Jalan Jalan',
        'kecamatan': 'Kecamatan',
        'kota': 'Kota',
        'provinsi': 'Provinsi',
        'restoran': 'Restoran',
        'jalan_restoran': 'Jalan Restoran',
        'kecamatan_restoran': 'Kecamatan Restoran',
        'kota_restoran': 'Kota Restoran',
        'provinsi_restoran': 'Provinsi Restoran',
        'daftar_makanan': [
            {
                'nama_makanan': 'Makanan 1',
                'jumlah_makanan': '1',
                'catatan_makanan': 'Catatan Makanan 1',
            },
            {
                'nama_makanan': 'Makanan 2',
                'jumlah_makanan': '2',
                'catatan_makanan': 'Catatan Makanan 2',
            },
        ],
        'total_harga': '50000',
        'total_diskon': '10000',
        'biaya_pengantaran': '10000',
        'total_biaya': '50000',
        'jenis_pembayaran': 'RestoPay',
        'status_pembayaran': 'Belum Dibayar',

        'kurir': '-',
        'plat_nomor': '-',
        'jenis_kendaraan': '-',
        'merk_kendaraan': '-',
    }
    return render(request, 'ringkasan_pesanan.html', context)


def konfirmasi_pembayaran(request):
    context = {
        'nama': 'Budi',
        'waktu_pemesanan': '2020-01-01 00:00:00',
        'status_pesanan': 'Menunggu Konfirmasi Restoran',
        'jalan': 'Jalan Jalan',
        'kecamatan': 'Kecamatan',
        'kota': 'Kota',
        'provinsi': 'Provinsi',
        'restoran': 'Restoran',
        'jalan_restoran': 'Jalan Restoran',
        'kecamatan_restoran': 'Kecamatan Restoran',
        'kota_restoran': 'Kota Restoran',
        'provinsi_restoran': 'Provinsi Restoran',
        'daftar_makanan': [
            {
                'nama_makanan': 'Makanan 1',
                'jumlah_makanan': '1',
                'catatan_makanan': 'Catatan Makanan 1',
            },
            {
                'nama_makanan': 'Makanan 2',
                'jumlah_makanan': '2',
                'catatan_makanan': 'Catatan Makanan 2',
            },
        ],
        'total_harga': '50000',
        'total_diskon': '10000',
        'biaya_pengantaran': '10000',
        'total_biaya': '50000',
        'sisa_waktu_pembayaran': '00:00:55',
        'jenis_pembayaran': 'RestoPay',
        'status_pembayaran': 'Menggu Pembayaran',

    }
    return render(request, 'konfirmasi_pembayaran.html', context)


def daftar_pesanan_makanan(request, rname, rbranch):

    context = {
        'daftar_pesanan_makanan': [
            {
                'Nama_Pesanan': 'Nasi Bakar',
                'Harga': '5000',
                'Jumlah': '1',
                'Total': '5000',
                'Metode_Pengantaran': 'Motor',
                'Metode_Pembayaran': 'RestoPay',
                'Total_Diskon': '0',
                'Biaya_Pengantaran': '4000',
                'Total_Biaya': '9000',

            },
        ]
    }
    return render(request, 'daftar_pesanan_makanan.html', context)


def pemilihan_pesanan_pada_restoran(request, rname, rbranch):
    cursor.execute(
        f'select foodname,price from  food where rname=\'{rname}\' and rbranch=\'{rbranch}\'')
    records = cursor.fetchall()
    context = {
        'records': records


    }
    return render(request, 'pemilihan_pesanan_pada_restoran.html', context)


def pengisian_alamat_pemesanan_makanan(request):
    form = FormPengisianAlamatMakanan(request.POST or None)
    if request.method == "POST":
        cursor.execute(f'select distinct province from delvery_fee_per_km')
        records = cursor.fetchall()
        context = {
            'form': form,
            'records': records

        }
        return render(request, 'pengisian_alamat_pemesanan_makanan.html', context)
    cursor.execute(f'select distinct province from delivery_fee_per_km')
    records = cursor.fetchall()
    
    context = {
        'form': form,
        'records': records

    }
    return render(request, 'pengisian_alamat_pemesanan_makanan.html', context)


def daftar_restoran_di_provinsi(request):
    province = request.get
    cursor.execute(f'select restaurant.rname,restaurant.rbranch,promo.promoname from restaurant,restaurant_promo,promo where restaurant.rname= restaurant_promo.rname and restaurant_promo.rbranch = restaurant_promo.rbranch and restaurant_promo.pid= promo.id')
    records = cursor.fetchall()
    # for i in range(len(records)):
    # for i in range(len(records_restoran)):
    #     cursor.execute(
    #         f'select * from promo where id = \'{records_restoran[i][8]}\' ')
    #     if len(cursor.fetchmany()) == 1:
    #         records_restoran[i] += ('Nama Promo', i+1)
    context = {
        'records': records
    }
    return render(request, 'daftar_restoran_di_provinsi.html', context)


def buat_kategori_makanan(request):
    form = FormBuatKategoriMakanan(request.POST or None)
    if request.method == "POST":
        nama = request.POST.get('nama')
        if form.is_valid():
            cursor.execute(
                f"SELECT MAX(CAST(id as DECIMAL)) from food_category")
            maxId = cursor.fetchall()[0][0]
            length = int(maxId) + 1
            cursor.execute(
                f'insert into food_category values (\'{length}\', \'{nama}\')')
            connection.commit()
            context = {
                'form': form,
            }
            return render(request, 'buat_kategori_makanan.html', context)
    context = {
        'form': form,
    }
    return render(request, 'buat_kategori_makanan.html', context)


def daftar_kategori_makanan(request):
    cursor.execute('select * from food_category')
    records = cursor.fetchall()
    records = sorted(records, key=lambda x: x[1].lower())
    for i in range(len(records)):
        cursor.execute(
            f'select * from food where fcategory = \'{records[i][0]}\'')
        if len(cursor.fetchmany()) == 1:
            records[i] += ('Makanan', i+1)

    context = {'records': records}
    return render(request, 'daftar_kategori_makanan.html', context)


def delete_kategori_makanan(request, id):
    cursor.execute(f'delete from food_category where id = \'{id}\'')
    connection.commit()
    return HttpResponseRedirect(reverse('trigger4:daftar_kategori_makanan'))
