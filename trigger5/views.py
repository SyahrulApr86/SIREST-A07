from django.shortcuts import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import *
from utils.query import *

# Create your views here.

def buat_kategori(request):
    if request.method == 'POST':
        new_kategori = request.POST.get('kategori')
        cursor.execute(f'select * restaurant_category')
        id = cursor.fetchmany() + 1

        cursor.execute(f""" 
            INSERT INTO RESTAURANT_CATEGORY VALUES
            ('{id}',
            '{request.POST.['kategori']}')
        """)

        return redirect('trigger5:daftar_kategori')

    return render(request, "buat_kategori.html")

def daftar_kategori(request):
    cursor.execute(f""" 
        SELECT * from restaurant_category;
    """)

    data_kategori_resto = cursor.fetchall()

    context = {
        'list_kategori_resto': data_kategori_resto,
    }
    return render(request, "daftar_kategori.html", context)

def pemesanan_kurir(request):
    return render(request, "pemesanan_kurir.html")

def detail_pemesanan_kurir(request):
    return render(request, "detail_pemesanan_kurir.html")

def buat_bahanmakanan(request):
    return render(request, "buat_bahanmakanan.html")

def daftar_bahanmakanan(request):
    return render(request, "daftar_bahanmakanan.html")    

def hapus_kategori(request,id):
    return redirect('trigger5:daftar_kategori')

