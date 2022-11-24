from django.shortcuts import render
from trigger4.forms import *

# Create your views here.
def pesanan_berlangsung(request):
    context = {
        'pesanan_berlangsung': [
            {
                'restoran' : 'Sego Berkat', 
                'waktu_pesanan_dibuat' : '2022-11-04 11:30:05',
                'status_pesanan' : 'Menunggu Konfirmasi Restoran',       
                
            },
            {
                'restoran' : 'Sego sami', 
                'waktu_pesanan_dibuat' : '2022-11-06 11:30:05',
                'status_pesanan' : 'Menunggu Konfirmasi Restoran', 
                
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

def daftar_pesanan_makanan(request):
    context = {
        'daftar_pesanan_makanan': [
            {
                'Nama_Pesanan' : 'Nasi Bakar', 
                'Harga' : '5000',
                'Jumlah' : '1',
                'Total' : '5000',    
                'Metode_Pengantaran':'Motor',
                'Metode_Pembayaran':'RestoPay',
                'Total_Diskon' : '0',
                'Biaya_Pengantaran' : '4000',
                'Total_Biaya' : '9000',
                
            },
        ]
    }
    return render(request, 'daftar_pesanan_makanan.html', context)
def pemilihan_pesanan_pada_restoran(request):
    context = {
        'daftar_makanan': [
            {
                'Nama_Makanan' : 'Nasi Bakar', 
                'Harga' : '50000'       
                
            },
            {
                'Nama_Makanan' : 'Nasi Rebus', 
                'Harga' : '6000' 
                
            },
            {
                'Nama_Makanan' : 'Nasi kuah', 
                'Harga' : '7000' 
                
            },
        ]
    }
    return render(request, 'pemilihan_pesanan_pada_restoran.html', context)
def pemilihan_pesanan_pada_restoran(request):
    context = {
        'daftar_makanan': [
            {
                'Nama_Makanan' : 'Nasi Bakar', 
                'Harga' : '50000'       
                
            },
            {
                'Nama_Makanan' : 'Nasi Rebus', 
                'Harga' : '6000' 
                
            },
            {
                'Nama_Makanan' : 'Nasi kuah', 
                'Harga' : '7000' 
                
            },
        ]
    }
    return render(request, 'pemilihan_pesanan_pada_restoran.html', context)

def pengisian_alamat_pemesanan_makanan(request):
    form = FormPengisianAlamatMakanan(request.POST or None)

    context = {
        'form': form,
    }

    return render(request, 'pengisian_alamat_pemesanan_makanan.html', context)

def daftar_restoran_di_provinsi(request):
    context = {
        'daftar_restoran': [
            {
                'Nama_Cabang_Restoran' : 'Sego Berkat Depok', 
                'Promo_Berlangsung' : 'Promo 17 Agustusan'       
                
            },
            {
                'Nama_Cabang_Restoran' : 'Bebek carok Bogor', 
                'Promo_Berlangsung' : '-' 
                
            },
            {
                'Nama_Cabang_Restoran' : 'Nasi rebus Bekasi', 
                'Promo_Berlangsung' : 'Promo Hidup Santuy' 
                
            },
        ]
    }
    return render(request, 'daftar_restoran_di_provinsi.html', context)
    
def buat_kategori_makanan(request):
    form = FormBuatKategoriMakanan(request.POST or None)

    context = {
        'form': form,
    }

    return render(request, 'buat_kategori_makanan.html', context)

def daftar_kategori_makanan(request):
    context = {
        'daftar_kategori_makanan': [
            {
                'nama': 'carnivore diet',                
                
            },
            {
                'nama': 'vegetarian',
                
            },
            {
                'nama': 'pemakan angin',          
                
            },
            {
                'nama': 'anti kolesterol',   
                
            },
            {
                'nama': 'murah meriah',                
                
            },
            {
                'nama': 'berkat masjid',            
                
            },
            {
                'nama': 'yang penting halal',            
                
            },
        ]
    }
    return render(request, 'daftar_kategori_makanan.html', context)