from django.shortcuts import render

# Create your views here.

def tarif_detail(request):
    context = {
        'nomor' : '1',
        'provinsi' : 'DKI Jakarta',
        'motor' : '6000',
        'mobil' : '7000',
    }
    return render(request, "read_tarif_pengiriman.html", context)

def makanan_detail(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "read_makanan.html")
    
def tambah_tarif(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "create_tarif_pengiriman.html")

def tambah_makanan(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "create_makanan.html")

def update_tarif(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "update_tarif_pengiriman.html")

def update_makanan(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "update_makanan.html")

def daftar_restoran(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "daftar_restoran_cust.html")

def menu_restoran_cust(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "menu_restoran_cust.html")

def detail_restoran(request):
    # context = {
    #     'nomor' : '1',
    #     'provinsi' : 'DKI Jakarta',
    #     'motor' : '6000',
    #     'mobil' : '7000',
    # }
    return render(request, "detail_restoran.html")
