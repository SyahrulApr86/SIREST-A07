from django.shortcuts import render
from trigger_2.forms import *
from utils.query import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.shortcuts import render, redirect

# Create your views here.


def saldo_restopay(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')
    cursor.execute(
        f"SELECT restopay FROM transaction_actor WHERE email = '{email}'")
    saldo = cursor.fetchall()[0][0]

    if request.COOKIES.get('role') == 'restaurant':
        role = 'restaurant'
    elif request.COOKIES.get('role') == 'admin':
        role = 'admin'
    elif request.COOKIES.get('role') == 'courier':
        role = 'courier'
    elif request.COOKIES.get('role') == 'customer':
        role = 'customer'

    context = {
        'saldo': saldo,
        'adminid': request.COOKIES.get('adminid'),
        'role': role,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
    }
    return render(request, 'saldo_restopay.html', context)


def isi_saldo(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')
    cursor.execute(
        f"select restopay, bankname, accountno from transaction_actor WHERE email = '{email}'")
    record = cursor.fetchall()[0]
    saldo = record[0]
    nama_bank = record[1]
    nomor_rekening = record[2]

    if request.COOKIES.get('role') == 'restaurant':
        role = 'restaurant'
    elif request.COOKIES.get('role') == 'admin':
        role = 'admin'
    elif request.COOKIES.get('role') == 'courier':
        role = 'courier'
    elif request.COOKIES.get('role') == 'customer':
        role = 'customer'

    if request.method == 'POST' or 'post' and not request.method == 'GET':
        saldo_pengisian = request.POST.get('saldo_pengisian')

        # cek saldo pengisian
        if saldo_pengisian == '':
            form = FormIsiSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Saldo Pengisian tidak boleh kosong',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }

            return render(request, 'isi_saldo.html', context)

        if not saldo_pengisian.isnumeric() and not None:
            form = FormIsiSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Input tidak valid',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'isi_saldo.html', context)

        if int(saldo_pengisian) <= 0:
            form = FormIsiSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Input tidak valid',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'isi_saldo.html', context)

        # insert ke database
        try:
            cursor.execute(
                f"UPDATE transaction_actor SET restopay = restopay + {saldo_pengisian} WHERE email = '{email}'")
            connection.commit()
            cursor.execute(
                f"select restopay, bankname, accountno from transaction_actor WHERE email = '{email}'")
            record = cursor.fetchall()[0]
            saldo = record[0]

            form = FormIsiSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Isi Saldo Berhasil',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'isi_saldo.html', context)

        except Exception as e:
            # rollback
            connection.rollback()
            form = FormIsiSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Isi Saldo Gagal',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'isi_saldo.html', context)

    form = FormIsiSaldo(request.POST or None)

    context = {
        'form': form,
        'saldo': saldo,
        'nama_bank': nama_bank,
        'nomor_rekening': nomor_rekening,
        'role': role,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
    }

    return render(request, 'isi_saldo.html', context)


def tarik_saldo(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')
    cursor.execute(
        f"select restopay, bankname, accountno from transaction_actor WHERE email = '{email}'")
    record = cursor.fetchall()[0]
    saldo = record[0]
    nama_bank = record[1]
    nomor_rekening = record[2]

    if request.COOKIES.get('role') == 'restaurant':
        role = 'restaurant'
    elif request.COOKIES.get('role') == 'admin':
        role = 'admin'
    elif request.COOKIES.get('role') == 'courier':
        role = 'courier'
    elif request.COOKIES.get('role') == 'customer':
        role = 'customer'

    if request.method == 'POST' or 'post' and not request.method == 'GET':
        saldo_penarikan = request.POST.get('saldo_penarikan')

        # cek saldo penarikan
        if saldo_penarikan == '':
            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Saldo Penarikan tidak boleh kosong',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)

        if not saldo_penarikan.isnumeric() and not None:
            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Input tidak valid',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)

        if int(saldo_penarikan) <= 0:
            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Input tidak valid',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)

        if int(saldo_penarikan) > saldo:
            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Saldo tidak mencukupi',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)

            # insert ke database
        try:
            cursor.execute(
                f"UPDATE transaction_actor SET restopay = restopay - {saldo_penarikan} WHERE email = '{email}'")
            connection.commit()
            cursor.execute(
                f"select restopay, bankname, accountno from transaction_actor WHERE email = '{email}'")
            record = cursor.fetchall()[0]
            saldo = record[0]

            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Tarik Saldo Berhasil',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)
        except Exception as e:
            # rollback
            connection.rollback()
            form = FormTarikSaldo(request.POST or None)

            context = {
                'form': form,
                'saldo': saldo,
                'nama_bank': nama_bank,
                'nomor_rekening': nomor_rekening,
                'message': 'Tarik Saldo Gagal',
                'role': role,
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
            }

            return render(request, 'tarik_saldo.html', context)

    form = FormTarikSaldo(request.POST or None)

    context = {
        'form': form,
        'saldo': saldo,
        'nama_bank': nama_bank,
        'nomor_rekening': nomor_rekening,
        'role': role,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
    }

    return render(request, 'tarik_saldo.html', context)


def daftar_pesanan(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')

    cursor.execute(
        f"""
        select concat(fname, ' ', lname), t.datetime, ts.name, ua.email
        from transaction t
        join user_acc ua on t.email = ua.email
        join transaction_history th on t.email = th.email and t.datetime = th.datetime
        join transaction_status ts on th.tsid = ts.id
        join transaction_food tf on t.email = tf.email and t.datetime = tf.datetime
        join restaurant r on tf.rname = r.rname and tf.rbranch = r.rbranch
        where th.datetimestatus = (select max(th2.datetimestatus) from transaction_history th2 where th2.email = th.email and th2.datetime = th.datetime)
        and r.email = '{email}'
        and ts.name != 'Pesanan Selesai'
        and ts.name != 'Pesanan Dibatalkan'
        group by r.email, t.datetime, ts.name, ua.fname, ua.lname, ua.email;"""
    )

    record = cursor.fetchall()

    if request.COOKIES.get('role') == 'restaurant':
        role = 'restaurant'
    elif request.COOKIES.get('role') == 'admin':
        role = 'admin'
    elif request.COOKIES.get('role') == 'courier':
        role = 'courier'
    elif request.COOKIES.get('role') == 'customer':
        role = 'customer'

    context = {
        'daftar_pesanan': record,
        'role': role,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
    }
    return render(request, 'daftar_pesanan.html', context)


def ubah_status_pesanan(request, email, datetime, status):
    cursor.execute('set search_path to sirest')
    if status == "Nunggu Konfirmasi Resto":
        status = 3
    elif status == "Pesanan Dibuat":
        status = 2
    elif status == "Pesanan Diantar":
        status = 5
    elif status == "Menunggu Kurir":
        status = 4
    elif status == "batal":
        status = 6

    try:
        connection.commit()
        cursor.execute(
            f"insert into transaction_history values ('{email}', '{datetime}', {status}, now())")
        connection.commit()

        if status == 4:
            cursor.execute(
                f"""
                select email
                from courier
                """
            )
            record = cursor.fetchall()
            # random courier
            courier = record[random.randint(0, len(record) - 1)][0]
            cursor.execute(
                f"""
                update transaction
                set courierid = '{courier}'
                where email = '{email}'
                and datetime = '{datetime}';
                """
            )
            connection.commit()
        #  back to daftar pesanan
        return HttpResponseRedirect(reverse('trigger_2:daftar_pesanan'))
    except Exception as e:
        # rollback
        connection.rollback()
        print(e)
        return HttpResponseRedirect(reverse('trigger_2:daftar_pesanan'))


def detail_pesanan(request, email, datetime):
    cursor.execute('set search_path to sirest')
    cursor.execute(
        f"""
            select datetime, concat(fname, ' ', lname), street, district, city, province, totalfood, totaldiscount, deliveryfee, totalprice, payment_method.name, payment_status.name
            from transaction, user_acc, payment_method, payment_status
            where transaction.pmid = payment_method.id
            and transaction.psid = payment_status.id
            and transaction.email = '{email}'
            and datetime = '{datetime}'
            and transaction.email = user_acc.email;
        """
    )
    record = cursor.fetchall()[0]
    waktu_pemesanan = record[0]
    nama = record[1]
    jalan = record[2]
    kecamatan = record[3]
    kota = record[4]
    provinsi = record[5]

    total_harga_makanan = record[6]
    total_diskon = record[7]
    biaya_pengiriman = record[8]
    total_harga = record[9]

    jenis_pembayaran = record[10]
    status_pembayaran = record[11]

    cursor.execute(
        f"""
            select rname, rbranch
            from transaction
            join transaction_food tf on transaction.email = tf.email and transaction.datetime = tf.datetime
            where transaction.email = '{email}'
            and transaction.datetime = '{datetime}'
            group by tf.rname, tf.rbranch;
        """
    )

    record = cursor.fetchall()[0]
    restoran = record[0]
    cabang_restoran = record[1]

    cursor.execute(
        f"""
            select street, district, city, province
            from restaurant
            where rname = '{restoran}'
            and rbranch = '{cabang_restoran}';
        """
    )

    record = cursor.fetchall()[0]
    jalan_restoran = record[0]
    kecamatan_restoran = record[1]
    kota_restoran = record[2]
    provinsi_restoran = record[3]

    cursor.execute(
        f"""
            select foodname, amount, note
            from transaction_food
            where email = '{email}'
            and datetime = '{datetime}'
            and rname = '{restoran}'
            and rbranch = '{cabang_restoran}';
        """
    )

    daftar_pesanan = cursor.fetchall()

    cursor.execute(
        f"""
            select name
            from transaction_history th, transaction_status ts
            where email = '{email}'
            and datetime = '{datetime}'
            and th.tsid = ts.id
            and datetimestatus = ((select max(th2.datetimestatus) from transaction_history th2 where th2.email = th.email and th2.datetime = th.datetime));
        """
    )

    record = cursor.fetchall()[0]
    status_pesanan = record[0]

    cursor.execute(
        f"""
            select concat(fname, ' ', lname), platenum, courier.vehicletype, vehiclebrand
            from courier, transaction, user_acc
            where courier.email = transaction.courierid
            and transaction.email = 'mhachef@java.com'
            and datetime = '2022-08-18 20:32:44.000000'
            and courier.email = user_acc.email;
        """
    )

    record = cursor.fetchall()
    if len(record) == 0:
        nama_kurir = None
        plat_nomor = None
        jenis_kendaraan = None
        merek_kendaraan = None
    else:
        nama_kurir = record[0][0]
        plat_nomor = record[0][1]
        jenis_kendaraan = record[0][2]
        merek_kendaraan = record[0][3]


    if request.COOKIES.get('role') == 'restaurant':
        role = 'restaurant'
    elif request.COOKIES.get('role') == 'admin':
        role = 'admin'
    elif request.COOKIES.get('role') == 'courier':
        role = 'courier'
    elif request.COOKIES.get('role') == 'customer':
        role = 'customer'
        
    context = {
        'role': role,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'waktu_pemesanan': waktu_pemesanan,
        'nama': nama,
        'jalan': jalan,
        'kecamatan': kecamatan,
        'kota': kota,
        'provinsi': provinsi,
        'total_harga_makanan': total_harga_makanan,
        'total_diskon': total_diskon,
        'biaya_pengiriman': biaya_pengiriman,
        'total_harga': total_harga,
        'jenis_pembayaran': jenis_pembayaran,
        'status_pembayaran': status_pembayaran,
        'restoran': restoran,
        'cabang_restoran': cabang_restoran,
        'daftar_pesanan': daftar_pesanan,
        'status_pesanan': status_pesanan,
        'jalan_restoran': jalan_restoran,
        'kecamatan_restoran': kecamatan_restoran,
        'kota_restoran': kota_restoran,
        'provinsi_restoran': provinsi_restoran,
        'nama_kurir': nama_kurir,
        'plat_nomor': plat_nomor,
        'jenis_kendaraan': jenis_kendaraan,
        'merk_kendaraan': merek_kendaraan,
    }
    return render(request, 'detail_pesanan.html', context)


def buat_jam_operasional(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')
    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')

    if request.method == 'POST' or 'post' and not request.method == 'GET':
        hari = request.POST.get('hari')
        jam_buka = request.POST.get('jam_buka')
        jam_tutup = request.POST.get('jam_tutup')

        # cek apakah jam buka dan jam tutup valid
        if not (jam_buka < jam_tutup):
            form = FormBuatJamOperasional(request.POST or None)
            context = {
                'form': form,
                'message': 'Jam buka dan jam tutup tidak valid',
                'role': 'restaurant',
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }
            return render(request, 'buat_jam_operasional.html', context)

        # cek apakah jam buka dan jam tutup sudah ada
        cursor.execute(
            f"""
                select *
                from restaurant_operating_hours
                where name = '{rname}'
                and branch = '{rbranch}'
                and day = '{hari}';
            """
        )
        record = cursor.fetchall()
        if len(record) != 0:
            form = FormBuatJamOperasional(request.POST or None)
            context = {
                'form': form,
                'message': 'Jam Operasional di hari tersebut sudah ada',
                'role': 'restaurant',
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }
            return render(request, 'buat_jam_operasional.html', context)

        # insert ke database
        try:
            cursor.execute(
                f"""
                    insert into restaurant_operating_hours
                    values ('{rname}', '{rbranch}', '{hari}', '{jam_buka}', '{jam_tutup}');
                """
            )
            connection.commit()

            # redirect ke halaman daftar jam operasional
            return redirect('trigger_2:daftar_jam_operasional')

        except Exception as e:
            # rollback
            print(e)
            connection.rollback()
            form = FormBuatJamOperasional(request.POST or None)
            context = {
                'form': form,
                'message': 'Gagal membuat jam operasional',
                'role': 'restaurant',
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }
            return render(request, 'buat_jam_operasional.html', context)

    form = FormBuatJamOperasional(request.POST or None)

    context = {
        'form': form,
        'role': 'restaurant',
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'email': request.COOKIES.get('email')
    }

    return render(request, 'buat_jam_operasional.html', context)


def daftar_jam_operasional(request):
    cursor.execute('set search_path to sirest')
    email = request.COOKIES.get('email')
    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')

    cursor.execute(
        f"""
            select *
            from restaurant_operating_hours
            where name = '{rname}'
            and branch = '{rbranch}';
        """
    )

    daftar_jam_operasional = cursor.fetchall()

    context = {
        'daftar_jam_operasional': daftar_jam_operasional,
        'role': 'restaurant',
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'email': request.COOKIES.get('email')
    }
    return render(request, 'daftar_jam_operasional.html', context)


def edit_jam_operasional(request, rname, rbranch, day):
    cursor.execute('set search_path to sirest')
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        jam_buka = request.POST.get('jam_buka')
        jam_tutup = request.POST.get('jam_tutup')

        # cek apakah jam buka dan jam tutup valid
        if not (jam_buka < jam_tutup):
            form = FormEditJamOperasional(request.POST or None)
            context = {
                'form': form,
                'message': 'Jam buka dan jam tutup tidak valid',
                'hari': day,
                'role': 'restaurant',
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }
            return render(request, 'edit_jam_operasional.html', context)

        # insert ke database
        try:
            cursor.execute(
                f"""
                    update restaurant_operating_hours
                    set starthours = '{jam_buka}',
                        endhours = '{jam_tutup}'
                    where name = '{rname}'
                    and branch = '{rbranch}'
                    and day = '{day}';
                """
            )
            connection.commit()

            # redirect ke halaman daftar jam operasional
            return redirect('trigger_2:daftar_jam_operasional')

        except Exception as e:
            # rollback
            print(e)
            connection.rollback()
            form = FormEditJamOperasional(request.POST or None)
            context = {
                'form': form,
                'message': 'Gagal mengubah jam operasional',
                'hari': day,
                'role': 'restaurant',
                'rname': request.COOKIES.get('rname'),
                'rbranch': request.COOKIES.get('rbranch'),
                'adminid': request.COOKIES.get('adminid'),
                'email': request.COOKIES.get('email')
            }
            return render(request, 'edit_jam_operasional.html', context)

    form = FormEditJamOperasional(request.POST or None)

    context = {
        'form': form,
        'hari': day,
        'role': 'restaurant',
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'email': request.COOKIES.get('email')
    }

    return render(request, 'edit_jam_operasional.html', context)

def hapus_jam_operasional(request, rname, rbranch, day):
    cursor.execute('set search_path to sirest')
    try:
        cursor.execute(
            f"""
                delete from restaurant_operating_hours
                where name = '{rname}'
                and branch = '{rbranch}'
                and day = '{day}';
            """
        )
        connection.commit()

        return redirect('trigger_2:daftar_jam_operasional')

    except Exception as e:
        print(e)
        connection.rollback()
        return redirect('trigger_2:daftar_jam_operasional')