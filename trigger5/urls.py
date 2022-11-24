from django.urls import path
from trigger5.views import *

app_name = 'trigger5'

urlpatterns = [
    path('buatkategori/', buat_kategori, name='buat_kategori'),
]