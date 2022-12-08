from django.shortcuts import render
from utils.query import *

# Create your views here.
def show_riwayat(request):
    return render(request, 'riwayat.html')

def show_detail_riwayat(request, id):
    # query riwayat by id
    return render(request, 'detail_riwayat.html')

def show_form_penilaian(request, id):
    return render(request, 'form_penilaian.html')

def show_buat_promo(request):
    return render(request, 'buat_promo.html')

def show_form_promo_minimum(request):
    return render(request, 'form_promo_minimum.html')

def show_form_promo_hari_spesial(request):
    return render(request, 'form_promo_hari_spesial.html')

def show_daftar_promo(request):
    cursor.execute('select * from promo')
    # TODO: GANTI FETCH ALL
    records_promo = cursor.fetchall()

    for i in range(len(records_promo)):
        cursor.execute(f'select * from special_day_promo where id = \'{records_promo[i][0]}\'')
        if len(cursor.fetchmany()) == 1:
            records_promo[i] += ('Promo Hari Spesial', i+1)
        cursor.execute(f'select * from min_transaction_promo where id = \'{records_promo[i][0]}\'')
        if len(cursor.fetchmany()) == 1:
            records_promo[i] += ('Promo Minimum Transaksi', i+1)

    context = {
        'records_promo':records_promo,
        'role':request.COOKIES.get('role'),
    }

    return render(request, 'daftar_promo.html', context)

def show_ubah_promo(request, id):

    return render(request, 'form_ubah_promosi.html')

def show_daftar_promo_restoran(request):
    return render(request, 'daftar_promo_restoran.html')

def show_form_promo_restoran(request):
    return render(request, 'form_promo_restoran.html')

def show_form_ubah_promo_restoran(request):
    return render(request, 'form_ubah_promo_restoran.html')

def show_detail_promo(request, id):
    cursor.execute(f'select * from promo where id = \'{id}\'')
    records_promo = cursor.fetchmany()

    cursor.execute(f'select * from special_day_promo where id = \'{records_promo[0][0]}\'')
    record = cursor.fetchmany()
    if len(record) == 1:
        records_promo[0] += ('Promo Hari Spesial', record[0][1])

    cursor.execute(f'select * from min_transaction_promo where id = \'{records_promo[0][0]}\'')
    record = cursor.fetchmany()
    if len(record) == 1:
        records_promo[0] += ('Promo Minimum Transaksi', record[0][1])
    
    print(records_promo)
    context = {
        'records_promo':records_promo[0],
        'role':request.COOKIES.get('role'),
    }

    return render(request, 'detail_promosi.html', context)

def show_detail_promo_restoran(request, id):
    return render(request, 'detail_promosi_restoran.html')