from django.shortcuts import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from account.forms import *
from utils.query import *
from datetime import datetime

def getFirst(x):
    return x[0]

# Create your views here.

def buat_kategori(request):
    role = request.COOKIES.get('role')
    #adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")

    if request.method == 'POST':
        cursor.execute(f'select id from restaurant_category;')
        all_id = cursor.fetchall()
        list_id = list(map(int,list(map(getFirst,all_id))))
        id = max(list_id)+1
        #print("what ",id)
        try :
            cursor.execute(f""" 
                INSERT INTO RESTAURANT_CATEGORY VALUES
                ('{id}',
                '{request.POST['kategori']}')
            """)
            connection.commit()
            return redirect('trigger5:daftar_kategori')
        except Exception as e :
            messages.error(request, e)
            connection.rollback()


            

    return render(request, "buat_kategori.html", {'role':request.COOKIES.get('role')})

def daftar_kategori(request):
    role = request.COOKIES.get('role')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    cursor.execute(f""" 
        SELECT * from restaurant_category;
    """)

    data_kategori_resto = cursor.fetchall()
    final_data_kategori_resto = []
    for cat in data_kategori_resto:
        cursor.execute(
            f'SELECT * from RESTAURANT_CATEGORY, RESTAURANT R where Rcategory = \'{cat[0]}\''
        )
        canDelete = (len(cursor.fetchall()) == 0)
        tuple_new = cat + (canDelete, )
        final_data_kategori_resto.append(tuple_new)

    print(final_data_kategori_resto)

    context = {
        'list_kategori_resto': final_data_kategori_resto,
        'role':request.COOKIES.get('role'),
    }
    return render(request, "daftar_kategori.html", context)

def hapus_kategori(request,id):
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    cursor.execute(f'DELETE from RESTAURANT_CATEGORY where id = \'{id}\'')

    return redirect('trigger5:daftar_kategori')


def pemesanan_kurir(request):
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'courier':
        return redirect("/")
    cursor.execute('set search_path to sirest')
    cursor.execute(f""" 
        SELECT Email, Datetime from TRANSACTION_HISTORY where tsid >= '4' except (SELECT Email, Datetime from TRANSACTION_HISTORY where tsid >= '5');
    """)

    data_transaksi = cursor.fetchall()
    # print("what ", len(data_transaksi))
    # cursor.execute(f"""SELECT Email, Datetime, TSID from TRANSACTION_HISTORY where tsid >= '4'""")
    # print(cursor.fetchall())
    # cursor.execute(f"""SELECT Email, Datetime, TSID from TRANSACTION_HISTORY where tsid >= '5'""")
    # print(cursor.fetchall())
    final_data_transaksi = []
    for tra in data_transaksi:
        cursor.execute(
            f'SELECT FName , LName from USER_ACC where email = \'{tra[0]}\''
        )
        simpan = cursor.fetchall()
        nama = simpan[0][0] + " " + simpan[0][1]

        cursor.execute(
            f'SELECT RName , RBranch FROM TRANSACTION_FOOD WHERE Email = \'{tra[0]}\' AND Datetime = \'{tra[1]}\''
        )
        simpan = cursor.fetchall()
        resto = simpan[0][0] + " " + simpan[0][1]

        new_tuple = (nama, resto, tra[1], tra[1].strftime("%Y-%m-%d %H:%M:%S") + " " + tra[0])
        final_data_transaksi.append(new_tuple)

    context = {
        'list_transaksi': final_data_transaksi,
        'role':request.COOKIES.get('role'),
        'adminid': adminid,
    }
    return render(request, "pemesanan_kurir.html", context)

def detail_pemesanan(request,id):
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'courier':
        return redirect("/")
    pk = id.split()
    email = pk[2]
    jam = pk[0] + " " + pk[1]
    cursor.execute(
        f'SELECT street, district, city, province, totalfood, totaldiscount, deliveryfee, totalprice, dfid, pmid, psid, courierid FROM TRANSACTION AS T WHERE T.Email = \'{email}\' AND T.Datetime = \'{jam}\';'
    )
    
    simpan = cursor.fetchall()
    jalan = simpan[0][0]
    kec = simpan[0][1]
    kota = simpan[0][2]
    prov = simpan[0][3]
    totalfood = simpan[0][4]
    totaldisc = simpan[0][5]
    deliveryfee = simpan[0][6]
    totalsemua = simpan[0][7]
    dfid = simpan[0][8]
    pmid = simpan[0][9]
    psid = simpan[0][10]
    courierid = simpan[0][11]

    cursor.execute(
        f'SELECT TF.rname, TF.rbranch FROM TRANSACTION_FOOD AS TF WHERE TF.Email = \'{email}\' AND TF.Datetime = \'{jam}\';'
    )
    simpan = cursor.fetchall()
    restoname = simpan[0][0]
    restobranch = simpan[0][1]
    namaresto = restoname + " " + restobranch
    cursor.execute(
        f'SELECT TF.foodname, TF.amount, TF.Note FROM TRANSACTION_FOOD AS TF WHERE TF.Email = \'{email}\' AND TF.Datetime = \'{jam}\';'
    )
    makanan = cursor.fetchall()

    cursor.execute(
        f'SELECT R.street, R.district, R.city, R.province FROM RESTAURANT AS R WHERE R.Rname = \'{restoname}\' AND R.RBranch = \'{restobranch}\';'
    )

    simpan = cursor.fetchall()
    jalanr = simpan[0][0]
    kecr = simpan[0][1]
    kotar = simpan[0][2]
    provr = simpan[0][3]

    cursor.execute(
        f'SELECT name FROM PAYMENT_METHOD WHERE Id= \'{pmid}\';'
    )

    simpan = cursor.fetchall()
    jenisbayar = simpan[0][0]

    cursor.execute(
        f'SELECT name FROM PAYMENT_STATUS WHERE Id= \'{psid}\';'
    )

    simpan = cursor.fetchall()
    statusbayar = simpan[0][0]

    cursor.execute(
        f'SELECT platenum, vehicletype,vehiclebrand FROM Courier WHERE email= \'{courierid}\';'
    )

    simpan = cursor.fetchall()
    plat = simpan[0][0]
    jeniskendaraan = simpan[0][1]
    merk = simpan[0][2]

    cursor.execute(
        f'SELECT fname, lname FROM user_acc WHERE email= \'{email}\';'
    )

    simpan = cursor.fetchall()
    nama = simpan[0][0] + " " + simpan[0][1]

    cursor.execute(
        f'SELECT fname, lname FROM user_acc WHERE email= \'{courierid}\';'
    )

    simpan = cursor.fetchall()
    namakurir = simpan[0][0] + " " + simpan[0][1]

    context = {
        'waktu' : jam,
        'nama' : nama,
        'jalan': jalan,
        'kec': kec,
        'kota': kota,
        'prov': prov,
        'resto': namaresto,
        'jalanr': jalanr,
        'kecr': kecr,
        'kotar': kotar,
        'provr': provr,
        'makanan': makanan,
        'totalfood': totalfood,
        'totaldisc': totaldisc,
        'deliveryfee': deliveryfee,
        'totalsemua': totalsemua,
        'jenisbayar': jenisbayar,
        'statusbayar': statusbayar,
        'kurir': namakurir,
        'plat': plat,
        'jeniskendaraan': jeniskendaraan,
        'merk': merk,
        'role':request.COOKIES.get('role'),
        'adminid': adminid,
    }
    return render(request, "detail_pemesanan_kurir.html", context)

def selesai_pemesanan(request, id):
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'courier':
        return redirect("/")
    pk = id.split()
    cursor.execute("SELECT now();")
    jam = cursor.fetchall()[0][0]
    cursor.execute(f""" 
            INSERT INTO TRANSACTION_HISTORY VALUES
            (
            '{pk[2]}',
            '{pk[0]+ " " + pk[1]}',
            '{'5'}',
            '{jam}'
            )
    """)

    return redirect('trigger5:pemesanan_kurir')

def buat_bahanmakanan(request):
    role = request.COOKIES.get('role')
    #adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    if request.method == 'POST':
        cursor.execute(f'select id from ingredient;')
        all_id = cursor.fetchall()
        list_id = list(map(int,list(map(getFirst,all_id))))
        id = max(list_id)+1
        #print("what ",id)

        try:
            cursor.execute(f""" 
            INSERT INTO INGREDIENT VALUES
            ('{id}',
            '{request.POST['bahan']}')
        """)

            return redirect('trigger5:daftar_bahanmakanan')
        except Exception as e :
            messages.error(request, e)
            connection.rollback()

    return render(request, "buat_bahanmakanan.html", {'role':request.COOKIES.get('role')})

def daftar_bahanmakanan(request):
    role = request.COOKIES.get('role')
    #adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    cursor.execute(f""" 
        SELECT * from ingredient;
    """)

    data_ingredient = cursor.fetchall()
    final_data_ingredient = []
    for ing in data_ingredient:
        cursor.execute(
            f'SELECT * from INGREDIENT, FOOD_INGREDIENT where Ingredient = \'{ing[0]}\''
        )
        canDelete = (len(cursor.fetchall()) == 0)
        tuple_new = ing + (canDelete, )
        final_data_ingredient.append(tuple_new)

    #print(final_data_ingredient)

    context = {
        'list_ingredient': final_data_ingredient,
        'role':request.COOKIES.get('role'),
        #'adminid': adminid,
        #'rname': request.COOKIES.get('rname'),
        #'rbranch': request.COOKIES.get('rbranch'),
    }
    return render(request, "daftar_bahanmakanan.html", context)

def hapus_bahanmakanan(request,id):
    role = request.COOKIES.get('role')
    #adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")
    cursor.execute(f'DELETE from INGREDIENT where id = \'{id}\'')

    return redirect('trigger5:daftar_bahanmakanan')


