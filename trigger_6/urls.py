from django.urls import path
from trigger_6.views import *

app_name = 'trigger_6'

urlpatterns = [
    path('', show_riwayat, name='show_riwayat'),
    path('detail/<email>/<datetime>', show_detail_riwayat, name='show_detail_riwayat'),
    path('penilaian/<email>/<datetime>', show_form_penilaian, name='show_form_penilaian'),
    path('buat-promo/', show_buat_promo, name='show_buat_promo'),
    path('buat-promo-minimum/', show_form_promo_minimum, name='show_form_promo_minimum'),
    path('buat-promo-hari-spesial/', show_form_promo_hari_spesial, name='show_form_promo_hari_spesial'),
    path('daftar-promo/', show_daftar_promo, name='show_daftar_promo'),
    path('ubah-promo/<jenis>/<id>', show_ubah_promo, name='show_ubah_promo'),
    path('daftar-promo-restoran/<rname>/<rbranch>', show_daftar_promo_restoran, name='show_daftar_promo_restoran'),
    path('daftar-promo-restoran/', show_daftar_promo_restoran, name='show_daftar_promo_restoran'),
    path('form-promo-restoran/', show_form_promo_restoran, name='show_form_promo_restoran'),
    path('form-ubah-promo-restoran/<id>', show_form_ubah_promo_restoran, name='show_form_ubah_promo_restoran'),
    path('detail-promo/<id>', show_detail_promo, name='show_detail_promo'),
    path('detail-promo-restoran/<rname>/<rbranch>/<id>', show_detail_promo_restoran, name='show_detail_promo_restoran'),
    path('delete-promo/<id>', delete_promo, name='delete_promo'),
    path('delete-promo-restoran/<rname>/<rbranch>/<id>', delete_promo_restoran, name='delete_promo_restoran'),
    path('ubah-form-input/', ubah_form_input, name='ubah_form_input')
]