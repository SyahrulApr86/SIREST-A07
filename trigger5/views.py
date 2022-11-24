from django.shortcuts import render

# Create your views here.

def buat_kategori(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "buat_kategori.html")
