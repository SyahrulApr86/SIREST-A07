from django.shortcuts import render

# Create your views here.

def buat_kategori(request):
    return render(request, "buat_kategori.html")

def daftar_kategori(request):
    return render(request, "daftar_kategori.html")

def pemesanan_kurir(request):
    return render(request, "pemesanan_kurir.html")

def detail_pemesanan_kurir(request):
    return render(request, "detail_pemesanan_kurir.html")

def buat_bahanmakanan(request):
    return render(request, "buat_bahanmakanan.html")

def daftar_bahanmakanan(request):
    return render(request, "daftar_bahanmakanan.html")
