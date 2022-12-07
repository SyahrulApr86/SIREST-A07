from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# TODO : ACTIVATE TRIGGER
def tambah_tarif(request):
    # if not is_authenticated(request) :
    #     return redirect("/")
    # else:
    #     role = request.session["role"]
    #     if role != 'admin':
    #         return redirect("/")

    if request.method == "POST":
        # try :
            
            with connection.cursor() as cursor:
                cursor.execute(f""" 
                    INSERT INTO DELIVERY_FEE_PER_KM VALUES
                    ('{request.POST['id_trf']}',
                    '{request.POST['province']}',
                    '{request.POST['motorfee']}',
                    '{request.POST['carfee']}')
                """)
            messages.add_message(request, messages.SUCCESS, 'Tarif Pengiriman Berhasil Ditambahkan')
            return redirect("/daftartarif")
        

    with connection.cursor() as c:
        c.execute(f""" 
            SELECT MAX(CAST(id as DECIMAL)) from delivery_fee_per_km;
        """)
        maxId = c.fetchall()[0][0]
        length = int(maxId) + 1
    return render(request, 'create_tarif_pengiriman.html', {'length': length})

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
    
# def tambah_tarif(request):
#     # context = {
#     #     'nomor' : '1',
#     #     'provinsi' : 'DKI Jakarta',
#     #     'motor' : '6000',
#     #     'mobil' : '7000',
#     # }
#     return render(request, "create_tarif_pengiriman.html")

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
