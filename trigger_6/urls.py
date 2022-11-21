from django.urls import path
from trigger_6.views import *

app_name = 'trigger_6'

urlpatterns = [
    path('', show_riwayat, name='show_riwayat'),
    path('detail/<id>', show_detail_riwayat, name='show_detail_riwayat'),
    path('penilaian/<id>', show_form_penilaian, name='show_form_penilaian'),
    path('buat-promo/', show_buat_promo, name='show_buat_promo'),
    path('buat-promo-minimum/', show_form_promo_minimum, name='show_form_promo_minimum'),
    path('buat-promo-hari-spesial/', show_form_promo_hari_spesial, name='show_form_promo_hari_spesial'),
    path('daftar-promo/', show_daftar_promo, name='show_daftar_promo'),
]