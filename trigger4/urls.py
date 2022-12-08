from django.urls import path
from trigger4.views import *

app_name = 'trigger4'

urlpatterns = [
    path('buat_kategori_makanan/', buat_kategori_makanan, name='buat_kategori_makanan'),
    path('daftar_kategori_makanan/', daftar_kategori_makanan, name='daftar_kategori_makanan'),
    path('pengisian_alamat_pemesanan_makanan/', pengisian_alamat_pemesanan_makanan, 
        name='pengisian_alamat_pemesanan_makanan'),
    path('daftar_restoran_di_provinsi/', daftar_restoran_di_provinsi, name='daftar_restoran_di_provinsi'),
    path('pemilihan_makanan_pada_restoran/', pemilihan_pesanan_pada_restoran, name='pemilihan_makanan_pada_restoran'),
    path('daftar_pesanan_makanan/', daftar_pesanan_makanan, name='daftar_pesanan_makanan'),
    path('konfirmasi_pembayaran/', konfirmasi_pembayaran, name='konfirmasi_pembayaran'),
    path('ringkasan_pesanan/', ringkasan_pesanan, name='ringkasan_pesanan'),
    path('pesanan_berlangsung/', pesanan_berlangsung, name='pesanan_berlangsung'),
]