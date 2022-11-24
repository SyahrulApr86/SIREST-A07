from django.urls import path
from trigger_2.views import *

app_name = 'trigger_2'

urlpatterns = [
    path('saldo_restopay/', saldo_restopay, name='saldo_restopay'),
    path('isi_saldo/', isi_saldo, name='isi_saldo'),
    path('tarik_saldo/', tarik_saldo, name='tarik_saldo'),
    path('daftar_pesanan/', daftar_pesanan, name='daftar_pesanan'),
    path('daftar_pesanan/<int:id_pesanan>/', detail_pesanan, name='detail_pesanan'),
    path('buat_jam_operasional/', buat_jam_operasional, name='buat_jam_operasional'),
    path('daftar_jam_operasional/', daftar_jam_operasional, name='daftar_jam_operasional'),
    path('daftar_jam_operasional/<int:id_jam_operasional>/',
         edit_jam_operasional, name='edit_jam_operasional'),
]



