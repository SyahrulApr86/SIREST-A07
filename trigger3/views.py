import json
from django.db import connection
from django.contrib import messages
from django.shortcuts import render, redirect
from utils.query import *

# Create your views here.


# TODO : ACTIVATE TRIGGER
def tambah_tarif(request):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")

    if request.method == "POST":
        try:
            cursor.execute(f""" 
                INSERT INTO DELIVERY_FEE_PER_KM VALUES
                ('{request.POST['id_trf']}',
                '{request.POST['province']}',
                '{request.POST['motorfee']}',
                '{request.POST['carfee']}')
            """)
            connection.commit()
            return redirect("/trigger3/daftartarif")
        except Exception as e:
            messages.error(request, e)
            connection.rollback()

    cursor.execute(f""" 
            SELECT MAX(CAST(id as DECIMAL)) from delivery_fee_per_km;
        """)
    maxId = cursor.fetchall()[0][0]
    length = int(maxId) + 1

    return render(request, 'create_tarif_pengiriman.html', {'length': length, 'role': request.COOKIES.get('role'), 'adminid': adminid, 'rname': request.COOKIES.get('rname'), 'rbranch': request.COOKIES.get('rbranch'),
                                                            })


def tarif_detail(request):
    cursor.execute('set search_path to sirest')
    cursor.execute(f'select * from DELIVERY_FEE_PER_KM')
    record = cursor.fetchall()
    context = {
        'dataTarif': record,
        'role': request.COOKIES.get('role'),
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),

    }
    return render(request, "read_tarif_pengiriman.html", context)


def makanan_resto(request):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')

    if role == None:
        return redirect("/login")
    if role != 'restaurant':
        return redirect("/")

    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')
    cursor.execute(
        f'select f.foodname, f.description, f.stock, f.price, fg.name, string_agg(i.name, \', \') from food f, food_category fg, food_ingredient fi, ingredient i where f.rbranch = \'{rbranch}\' and f.rname = \'{rname}\' and  fg.id = f.fcategory and f.rbranch = fi.rbranch and f.rname = fi.rname and f.foodname = fi.foodname and fi.Ingredient = i.id group by f.foodname, f.description, f.stock, f.price,  fg.name')
    record = cursor.fetchall()

    cursor.execute(
        f'select foodname from food where rbranch = \'{rbranch}\' and rname = \'{rname}\' and (rname, rbranch, foodname) not in (select distinct rname, rbranch, foodname from transaction_food) ')
    deletable = cursor.fetchall()

    foodArr = []
    for food in deletable:
        foodArr.append(food[0])

    context = {
        'deletable_food': foodArr,
        'dataMakanan': record,
        'role': request.COOKIES.get('role'),
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
    }

    return render(request, "read_makanan.html", context)


def update_tarif(request, id):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")

    cursor.execute(f'select * from delivery_fee_per_km where id = \'{id}\'')
    record = cursor.fetchall()

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
        except Exception as e:
            messages.error(request, e)
            connection.rollback()

    context = {
        'provinsi': record[0][1],
        'motorfee': record[0][2],
        'carfee': record[0][3],
        'role': request.COOKIES.get('role'),
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
    }
    return render(request, "update_tarif_pengiriman.html", context)


def delete_tarif(request, id):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    if role == None:
        return redirect("/login")
    if role != 'admin':
        return redirect("/")

    cursor.execute(f'select * from delivery_fee_per_km where id = \'{id}\'')
    record = cursor.fetchall()

    cursor.execute(f"""
        DELETE FROM DELIVERY_FEE_PER_KM
        WHERE id = '{id}';
    """)
    connection.commit()
    return redirect("/trigger3/daftartarif")


def tambah_makanan(request):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role != 'restaurant':
        return redirect("/")

    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')

    if request.method == "POST":

        category = request.POST['kategoriMakanan']
        cursor.execute(
            f'select id FROM food_category where name = \'{category}\'  ')
        idCategory = cursor.fetchmany()

        cursor.execute(f""" 
                    INSERT INTO FOOD VALUES
                    ('{rname}',
                    '{rbranch}',
                    '{request.POST['nama']}',
                    '{request.POST['deskripsi']}',
                    '{request.POST['stok']}',
                    '{request.POST['harga']}',
                    '{idCategory[0][0]}'
                    )
                """)
        connection.commit()

        click = request.POST['click']

        for x in range(int(click)):
            ingredient = request.POST[f'select-{x}']
            cursor.execute(
                f'select id FROM ingredient where name = \'{ingredient}\'  ')
            idBahan = cursor.fetchmany()

            cursor.execute(f""" 
                    INSERT INTO FOOD_INGREDIENT VALUES
                    ('{rname}',
                    '{rbranch}',
                    '{request.POST['nama']}',
                    '{idBahan[0][0]}'
                    )
                """)
            connection.commit()

        return redirect("/trigger3/daftarmakanan")

    cursor.execute(f'select name FROM FOOD_CATEGORY')
    kategoriAll = cursor.fetchall()
    cursor.execute(f'select name FROM INGREDIENT')
    bahanAll = cursor.fetchall()

    context = {
        'kategoriMakanan': kategoriAll,
        'jsonBahan': json.dumps(bahanAll),
        'bahanMakanan': bahanAll,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'role': role
    }
    return render(request, "create_makanan.html", context)


def update_makanan(request, foodname):
    cursor.execute('set search_path to sirest')
    adminid = request.COOKIES.get('adminid')
    role = request.COOKIES.get('role')
    if role == None:
        return redirect("/login")
    if role != 'restaurant':
        return redirect("/")

    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')

    cursor.execute(f'select * from food where foodname = \'{foodname}\'')
    record = cursor.fetchall()

    if request.method == "POST":

        # Update food nya
        category = request.POST['kategoriMakanan']
        cursor.execute(
            f'select id FROM food_category where name = \'{category}\'  ')
        idCategory = cursor.fetchmany()

        cursor.execute(f"""
            UPDATE FOOD
            SET Description = '{request.POST['deskripsi']}',
            Stock = '{request.POST['stok']}',
            price = '{request.POST['harga']}',
            fcategory = '{idCategory[0][0]}'
            WHERE foodname = '{foodname}';
                    """)
        connection.commit()

        # Delete bahan dari db yang user delete
        bahanDelete = request.POST['deleteBahan']
        bahanArr = (bahanDelete.split(","))
        bahanArr.remove("")

        for bahan in bahanArr:
            cursor.execute(
                f'select id FROM ingredient where name = \'{bahan}\'  ')
            bahanIns = cursor.fetchall()

            cursor.execute(f"""
                DELETE FROM food_ingredient
                WHERE ingredient = '{bahanIns[0][0]}';
            """)
            connection.commit()

        # Tambah bahan ke db
        click = request.POST['click']
        for x in range(int(click)):
            ingredient = request.POST[f'select-{x}']
            cursor.execute(
                f'select id FROM ingredient where name = \'{ingredient}\'  ')
            idBahan = cursor.fetchmany()

            cursor.execute(f""" 
                INSERT INTO FOOD_INGREDIENT VALUES
                    ('{rname}',
                    '{rbranch}',
                    '{foodname}',
                    '{idBahan[0][0]}'
                    )
                """)
            connection.commit()

        return redirect("/trigger3/daftarmakanan")

    cursor.execute(f'select name FROM FOOD_CATEGORY')
    kategoriAll = cursor.fetchall()
    cursor.execute(f'select name FROM INGREDIENT')
    bahanAll = cursor.fetchall()
    cursor.execute(
        f'select i.name FROM food_ingredient fi, ingredient i where fi.foodname = \'{foodname}\' and fi.ingredient = i.id')
    bahanSelected = cursor.fetchall()

    context = {
        'foodname': record[0][2],
        'description': record[0][3],
        'stock': record[0][4],
        'price': record[0][5],
        'foodcategory': record[0][6],
        'bahanMakanan': bahanAll,
        'jsonBahan': json.dumps(bahanAll),
        'kategoriMakanan': kategoriAll,
        'bahanUsed': bahanSelected,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'role': role
    }
    return render(request, "update_makanan.html", context)


def delete_makanan(request, foodname):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    if role == None:
        return redirect("/login")
    if role != 'restaurant':
        return redirect("/")

    cursor.execute(f"""
        DELETE FROM FOOD
        WHERE FoodName = '{foodname}'
        AND RName = \'{request.COOKIES.get('rname')}\'
        AND RBranch = \'{request.COOKIES.get('rbranch')}\';
    """)
    connection.commit()
    return redirect("/trigger3/daftarmakanan")


def daftar_restoran(request):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role == 'restaurant':
        return redirect("/")

    cursor.execute(f'select * from restaurant')
    record = cursor.fetchall()
    context = {
        'dataRestoran': record,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'role': role
    }
    return render(request, "daftar_restoran_cust.html", context)


def menu_restoran_cust(request, rname, rbranch):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role == 'restaurant':
        return redirect("/")

    cursor.execute(
        f'select f.foodname, f.description, f.stock, f.price, fg.name, string_agg(i.name, \', \') from food f, food_category fg, food_ingredient fi, ingredient i where f.stock > 0 and f.rbranch = \'{rbranch}\' and f.rname = \'{rname}\' and  fg.id = f.fcategory and f.rbranch = fi.rbranch and f.rname = fi.rname and f.foodname = fi.foodname and fi.Ingredient = i.id group by f.foodname, f.description, f.stock, f.price,  fg.name')
    record = cursor.fetchall()
    context = {
        'dataMenu': record,
        'rname': rname,
        'rbranch': rbranch,
        'adminid': request.COOKIES.get('adminid'),
        'role': role
    }
    return render(request, "menu_restoran_cust.html", context)


def detail_restoran(request, rname, rbranch):
    cursor.execute('set search_path to sirest')
    role = request.COOKIES.get('role')
    adminid = request.COOKIES.get('adminid')
    if role == None:
        return redirect("/login")
    if role == 'restaurant':
        return redirect("/")

    cursor.execute(
        f'select * from restaurant r, restaurant_category rc, restaurant_operating_hours ros where r.rname = \'{rname}\' and r.rbranch = \'{rbranch}\' and r.rcategory = rc.id and r.rname = ros.name and r.rbranch = ros.branch')
    records = cursor.fetchmany()
    context = {
        'dataRestoran': records,
        'rname': request.COOKIES.get('rname'),
        'rbranch': request.COOKIES.get('rbranch'),
        'adminid': request.COOKIES.get('adminid'),
        'role': role
    }

    return render(request, "detail_restoran.html", context)
