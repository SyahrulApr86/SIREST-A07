from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect
from utils.query import *

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
    role = request.COOKIES.get('role')
    # role = request.session["role"]
    print(role)
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    

    
    if request.method == "POST":
        
        try :
            cursor.execute(f""" 
                    INSERT INTO DELIVERY_FEE_PER_KM VALUES
                    ('{request.POST['id_trf']}',
                    '{request.POST['province']}',
                    '{request.POST['motorfee']}',
                    '{request.POST['carfee']}')
                """)
            connection.commit()
            return redirect("/trigger3/daftartarif")
        except Exception as e :
            messages.error(request, e)
            connection.rollback()

    cursor.execute(f""" 
            SELECT MAX(CAST(id as DECIMAL)) from delivery_fee_per_km;
        """)
    maxId = cursor.fetchall()[0][0]
    length = int(maxId) + 1
    
    
    return render(request, 'create_tarif_pengiriman.html', {'length': length})


def tarif_detail(request):
    cursor.execute(f'select * from DELIVERY_FEE_PER_KM')
    record = cursor.fetchall()
    print(record)
    context = {
        'dataTarif' : record,
    }
    return render(request, "read_tarif_pengiriman.html", context)

def makanan_detail(request):
    cursor.execute(f'select * from food f, food_category fg where fg.id = f.fcategory')
    record = cursor.fetchall()
    cursor.execute(f'select i.name from food f, food_ingredient fi, ingredient i where f.rname = fi.rname and f.rbranch = fi.rbranch and f.foodname = fi.foodname and fi.Ingredient = i.id')
    bahan = cursor.fetchall()
    # print(record)
    context = {
        'dataMakanan' : record,
        'dataBahan' : bahan
    }
    print(bahan)
    
    return render(request, "read_makanan.html", context)
    
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

def update_tarif(request, id):
    # print(request.POST['motorfee'])
    cursor.execute(f'select * from delivery_fee_per_km where id = \'{id}\'')
    record = cursor.fetchall()
    print(record)
    
    if request.method == "POST":
        try:
            cursor.execute(f"""
                        UPDATE DELIVERY_FEE_PER_KM
                        SET motorfee = '{request.POST['motorfee']}',
                        carfee = '{request.POST['carfee']}'
                        WHERE id = '{id}';
                        """)
            connection.commit()
            return redirect("/trigger3/daftartarif")
        except Exception as e :
            messages.error(request, e)
            connection.rollback()
            # cursor.execute("ROLLBACK")
            # connection.commit()

    context = {
        'provinsi' : record[0][1],
        'motorfee' : record[0][2],
        'carfee' : record[0][3],
    }
    return render(request, "update_tarif_pengiriman.html", context)

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
