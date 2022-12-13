from django.urls import path
from trigger3.views import tarif_detail, tambah_tarif, update_tarif, tambah_makanan, update_makanan, makanan_resto, daftar_restoran, menu_restoran_cust, detail_restoran, delete_tarif, delete_makanan

app_name = 'trigger3'

urlpatterns = [
    path('daftartarif/', tarif_detail, name='tarif_detail'),
    path('tambahtarif/', tambah_tarif, name='tambah_tarif'),
    path('updatetarif/<int:id>', update_tarif, name='update_tarif'),
    path('deletetarif/<int:id>', delete_tarif, name='delete_tarif'),
    # path('daftarmakanan/<str:rname>/<str:rbranch>', makanan_resto, name='makanan_resto'),
    path('daftarmakanan/', makanan_resto, name='makanan_resto'),
    path('tambahmakanan/', tambah_makanan, name='tambah_makanan'),
    path('updatemakanan/<str:foodname>', update_makanan, name='update_makanan'),
    path('deletemakanan/<str:foodname>', delete_makanan, name='delete_makanan'),
    path('daftarresto/', daftar_restoran, name='daftar_restoran'),
    path('menurestoran/<str:rname>/<str:rbranch>', menu_restoran_cust, name='menu_restoran_cust'),
    path('detailrestoran/<str:rname>/<str:rbranch>', detail_restoran, name='detail_restoran'),
]