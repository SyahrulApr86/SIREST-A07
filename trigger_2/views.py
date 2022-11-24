from django.shortcuts import render
from trigger_2.forms import *

# Create your views here.


def saldo_restopay(request):
    context = {
        'saldo': '1000000',
    }
    return render(request, 'saldo_restopay.html', context)


def isi_saldo(request):
    form = FormIsiSaldo(request.POST or None)

    context = {
        'form': form,
        'saldo': '1000000',
        'nama_bank': 'BRI',
        'nomor_rekening': '123456789',
    }

    return render(request, 'isi_saldo.html', context)


def tarik_saldo(request):
    form = FormTarikSaldo(request.POST or None)

    context = {
        'form': form,
        'saldo': '1000000',
        'nama_bank': 'BRI',
        'nomor_rekening': '123456789',
    }

    return render(request, 'tarik_saldo.html', context)


def daftar_pesanan(request):
    context = {
        'daftar_pesanan': [
            {
                'nama': 'Budi',
                'waktu_pemesanan': '2020-01-01 00:00:00',
                'status_pesanan': 'Pesanan Dibuat',
            }
        ]
    }
    return render(request, 'daftar_pesanan.html', context)


def detail_pesanan(request, id_pesanan):
    context = {
        'id_pesanan': id_pesanan,
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
        'status_pesanan': 'Belum Diantar',

        'kurir': '-',
        'plat_nomor': '-',
        'jenis_kendaraan': '-',
        'merk_kendaraan': '-',
    }
    return render(request, 'detail_pesanan.html', context)


def buat_jam_operasional(request):
    form = FormBuatJamOperasional(request.POST or None)

    context = {
        'form': form,
    }

    return render(request, 'buat_jam_operasional.html', context)


def daftar_jam_operasional(request):
    context = {
        'daftar_jam_operasional': [
            {
                'hari': 'Senin',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Selasa',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Rabu',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Kamis',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Jumat',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Sabtu',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
            {
                'hari': 'Minggu',
                'jam_buka': '08:00:00',
                'jam_tutup': '16:00:00',
            },
        ]
    }
    return render(request, 'daftar_jam_operasional.html', context)


def edit_jam_operasional(request, id_jam_operasional):
    form = FormEditJamOperasional(request.POST or None)

    context = {
        'form': form,
        'id_jam_operasional': id_jam_operasional,
        'hari': 'Senin',
        'jam_buka': '08:00:00',
        'jam_tutup': '16:00:00',
    }

    return render(request, 'edit_jam_operasional.html', context)
