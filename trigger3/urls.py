from django.urls import path
from trigger3.views import tarif_detail, tambah_tarif, update_tarif, tambah_makanan, update_makanan, makanan_detail, daftar_restoran, menu_restoran_cust, detail_restoran

app_name = 'trigger3'

urlpatterns = [
    path('/daftartarif', tarif_detail, name='tarif_detail'),
    path('/tambahtarif', tambah_tarif, name='tambah_tarif'),
    path('/updatetarif', update_tarif, name='update_tarif'),
    path('/daftarmakanan', makanan_detail, name='makanan_detail'),
    path('/tambahmakanan', tambah_makanan, name='tambah_makanan'),
    path('/updatemakanan', update_makanan, name='update_makanan'),
    path('/daftarresto', daftar_restoran, name='daftar_restoran'),
    path('/menurestoran', menu_restoran_cust, name='menu_restoran_cust'),
    path('/detailrestoran', detail_restoran, name='detail_restoran'),
]