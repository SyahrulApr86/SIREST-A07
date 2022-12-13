from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from utils.query import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_riwayat(request):
    role = request.COOKIES.get('role')
    email = request.COOKIES.get('email')

    if role == 'restaurant':
        rname = request.COOKIES.get('rname')
        rbranch = request.COOKIES.get('rbranch')
        sql = f'''select u.fname, u.lname, r.rname, r.rbranch, t.datetime, t.rating, foo.fname, foo.lname, ts.name, t.email from transaction t, transaction_history th, courier co, customer cu, 
        transaction_food tf, restaurant r, user_acc u, (select ua.email, ua.fname, ua.lname from user_acc ua) as foo, transaction_status ts where (t.email, t.datetime) = (th.email, th.datetime) 
        and t.courierid = co.email and t.email = cu.email and (t.email, t.datetime) = (tf.email, tf.datetime) and (r.rname, r.rbranch) = (tf.rname, tf.rbranch) and t.email = u.email and co.email
         = foo.email and th.tsid = ts.id and ts.id in ('5', '6') and tf.rname = \'{rname}\' and tf.rbranch = \'{rbranch}\''''
        cursor.execute(sql)
        record = cursor.fetchall()
    elif role == 'courier':
        sql = f'''select u.fname, u.lname, r.rname, r.rbranch, t.datetime, t.rating, foo.fname, foo.lname, ts.name, t.email from transaction t, transaction_history th, courier co, customer cu, 
        transaction_food tf, restaurant r, user_acc u, (select ua.email, ua.fname, ua.lname from user_acc ua) as foo, transaction_status ts where (t.email, t.datetime) = (th.email, th.datetime) 
        and t.courierid = co.email and t.email = cu.email and (t.email, t.datetime) = (tf.email, tf.datetime) and (r.rname, r.rbranch) = (tf.rname, tf.rbranch) and t.email = u.email and co.email
         = foo.email and th.tsid = ts.id and ts.id in ('5', '6') and co.email = \'{email}\''''
        cursor.execute(sql)
        record = cursor.fetchall()
    elif role == 'customer':
        sql = f'''select u.fname, u.lname, r.rname, r.rbranch, t.datetime, t.rating, foo.fname, foo.lname, ts.name, t.email from transaction t, transaction_history th, courier co, customer cu, 
        transaction_food tf, restaurant r, user_acc u, (select ua.email, ua.fname, ua.lname from user_acc ua) as foo, transaction_status ts where (t.email, t.datetime) = (th.email, th.datetime) 
        and t.courierid = co.email and t.email = cu.email and (t.email, t.datetime) = (tf.email, tf.datetime) and (r.rname, r.rbranch) = (tf.rname, tf.rbranch) and t.email = u.email and co.email
         = foo.email and th.tsid = ts.id and ts.id in ('5', '6') and t.email = \'{email}\''''
        cursor.execute(sql)
        record = cursor.fetchall()
    else:
        return redirect('/')

    context = {
        'role':role,
        'rname':request.COOKIES.get('rname'),
        'rbranch':request.COOKIES.get('rbranch'),
        'record':record,
    }
    print(record)
    return render(request, 'riwayat.html', context)

def show_detail_riwayat(request, email, datetime):
    # query riwayat by id
    sql = f'''select u.fname, u.lname, t.street, t.district, t.city, t.province, r.rname, r.rbranch, t.datetime, t.rating, foo.fname, foo.lname, co.platenum, co.vehicletype, co.vehiclebrand, 
    r.street, r.district, r.city, r.province, t.totalfood, t.totaldiscount, t.deliveryfee, t.totalprice, pm.name, ps.name from transaction t, courier co, transaction_food tf,  
    customer cu, restaurant r, user_acc u, (select ua.email, ua.fname, ua.lname from user_acc ua) as foo, payment_method pm, payment_status ps where t.courierid = co.email and t.email = cu.email and t.email = u.email and co.email
      = foo.email and pm.id = t.pmid and ps.id = t.psid and t.email = \'{email}\' and t.datetime = \'{datetime}\' and (r.rname, r.rbranch) = (tf.rname, tf.rbranch) and (t.email, t.datetime) = (tf.email, tf.datetime);
    '''
    cursor.execute(sql)
    record_riwayat = cursor.fetchall()

    cursor.execute(f'select tf.foodname, tf.note, tf.amount from transaction_food tf where tf.email = \'{email}\' and tf.datetime = \'{datetime}\';')
    ordered_food = cursor.fetchall()
    cursor.execute(f'select ts.name, th.datetimestatus from transaction_status ts, transaction_history th where ts.id = th.tsid and th.email = \'{email}\' and th.datetime = \'{datetime}\'')
    transaction_status = cursor.fetchall()

    for i in range(len(transaction_status)):
        transaction_status[i] = list(transaction_status[i])
        transaction_status[i][1] = transaction_status[i][1].strftime("%m/%d/%Y %H:%M:%S")

    context = {
        'record_riwayat':record_riwayat,
        'ordered_food':ordered_food,
        'transaction_status':transaction_status,
        'status':transaction_status[-1][0],
        'role':request.COOKIES.get('role'),
        'rname':request.COOKIES.get('rname'),
        'rbranch':request.COOKIES.get('rbranch'),
    }
    print('masuk')
    print(record_riwayat)
    print(ordered_food)
    print(transaction_status)
    return render(request, 'detail_riwayat.html', context)

def show_form_penilaian(request, email, datetime):
    if request.method == 'POST':
        rating = request.POST.get('nilai')
        if rating != '0':
            cursor.execute(f'update transaction set rating = \'{rating}\' where email = \'{email}\' and datetime = \'{datetime}\'')
            connection.commit()
            return HttpResponseRedirect(reverse('trigger_6:show_riwayat'))
        else:
            context = {
                'status':'error',
                'message':'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
                'role':request.COOKIES.get('role')
            }
            return render(request, 'form_penilaian.html', context)

    return render(request, 'form_penilaian.html', {'role':request.COOKIES.get('role')})

def show_buat_promo(request):
    return render(request, 'buat_promo.html', {'role':request.COOKIES.get('role')})

def show_form_promo_minimum(request):
    if request.method == "POST":
        name = request.POST.get('name')
        discount = request.POST.get('discount')
        mintransaction = request.POST.get('mintransaction')
        if (name == '' or discount == '' or mintransaction == ''):
            context = {
                'status':'error',
                'message':'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
                'role':request.COOKIES.get('role')
            }
            return render(request, 'form_promo_minimum.html', context)
        else:
            cursor.execute(f"SELECT MAX(CAST(id as DECIMAL)) from promo")
            maxId = cursor.fetchall()[0][0]
            length = int(maxId) + 1
            cursor.execute(f'insert into promo values (\'{length}\', \'{name}\', \'{discount}\')')
            connection.commit()
            cursor.execute(f'insert into min_transaction_promo values (\'{length}\', \'{mintransaction}\')')
            connection.commit()
            return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo'))
            
    return render(request, 'form_promo_minimum.html', {'role':request.COOKIES.get('role')})

def show_form_promo_hari_spesial(request):
    if request.method == "POST":
        name = request.POST.get('name')
        discount = request.POST.get('discount')
        date = request.POST.get('date')
        if (name == '' or discount == '' or date == ''):
            context = {
                'status':'error',
                'message':'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
                'role':request.COOKIES.get('role')
            }
            return render(request, 'form_promo_hari_spesial.html', context)
        else:
            cursor.execute(f"SELECT MAX(CAST(id as DECIMAL)) from promo")
            maxId = cursor.fetchall()[0][0]
            length = int(maxId) + 1
            cursor.execute(f'insert into promo values (\'{length}\', \'{name}\', \'{discount}\')')
            connection.commit()
            cursor.execute(f'insert into special_day_promo values (\'{length}\', \'{date}\')')
            connection.commit()
            return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo'))
            
    return render(request, 'form_promo_hari_spesial.html', {'role':request.COOKIES.get('role')})

def show_daftar_promo(request):
    cursor.execute('select * from promo')
    # TODO: GANTI FETCH ALL
    records_promo = cursor.fetchall()
    records_promo = sorted(records_promo, key=lambda x:x[1].lower())
    print(records_promo)

    for i in range(len(records_promo)):
        cursor.execute(f'select * from special_day_promo where id = \'{records_promo[i][0]}\'')
        if len(cursor.fetchmany()) == 1:
            records_promo[i] += ('Promo Hari Spesial', i+1)
        cursor.execute(f'select * from min_transaction_promo where id = \'{records_promo[i][0]}\'')
        if len(cursor.fetchmany()) == 1:
            records_promo[i] += ('Promo Minimum Transaksi', i+1)

        cursor.execute(f'select count(*) from restaurant_promo r where r.pid = \'{records_promo[i][0]}\'')
        record = cursor.fetchall()
        records_promo[i] += record[0]

    context = {
        'records_promo':records_promo,
        'role':request.COOKIES.get('role'),
        'rname':request.COOKIES.get('rname'),
        'rbranch':request.COOKIES.get('rbranch'),
    }

    return render(request, 'daftar_promo.html', context)

def show_ubah_promo(request, jenis, id):
    cursor.execute(f'select promoname from promo where id = \'{id}\'')
    record = cursor.fetchall()
    if request.method == 'POST':
        discount = request.POST.get('discount')

        if jenis == 'Promo Minimum Transaksi':
            mintransaction = request.POST.get('mintransaction')
        else:
            mintransaction = '-'

        if discount == '' or mintransaction == '':
            context = {
                'jenis_promo':jenis,
                'nama_promo':record[0][0],
                'status':'error',
                'message':'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
                'role':request.COOKIES.get('role')
            }
            return render(request, 'form_ubah_promosi.html', context)
        else:
            cursor.execute(f'update promo set discount = \'{discount}\' where id = \'{id}\'')
            connection.commit()
            if jenis == 'Promo Minimum Transaksi':
                cursor.execute(f'update min_transaction_promo set minimumtransactionnum = \'{mintransaction}\' where id = \'{id}\'')
                connection.commit()
            return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo'))

    
    context = {
        'jenis_promo':jenis,
        'nama_promo':record[0][0],
        'role':request.COOKIES.get('role'),
    }
    return render(request, 'form_ubah_promosi.html', context)

def show_daftar_promo_restoran(request, rname, rbranch):
    cursor.execute('set search_path to sirest')
    cursor.execute(f'select * from promo p, restaurant_promo r where p.id = r.pid and r.rname = \'{rname}\' and r.rbranch = \'{rbranch}\'')
    records_promo_resto = cursor.fetchall()
    print(len(records_promo_resto))

    for i in range(len(records_promo_resto)):
        records_promo_resto_list = list(records_promo_resto[i])
        records_promo_resto_list[6] = records_promo_resto_list[6].date()
        records_promo_resto_list[7] = records_promo_resto_list[7].date()
        records_promo_resto[i] = records_promo_resto_list

    context = {
        'records_promo_resto':records_promo_resto,
        'role':request.COOKIES.get('role'),
        'rname':rname,
        'rbranch':rbranch,
        'empty':len(records_promo_resto)
    }

    return render(request, 'daftar_promo_restoran.html', context)

def show_form_promo_restoran(request):
    cursor.execute('set search_path to sirest')
    rname = request.COOKIES.get('rname')
    rbranch = request.COOKIES.get('rbranch')
    cursor.execute('select promoname, id from promo')
    record_promoname = cursor.fetchall()

    if request.method == 'POST':
        try:
            if len(request.POST) != 5:
                raise Exception('Harap isi semua field yang ada.')

            pid = request.POST.get('name')
            startdate = request.POST.get('startdate')
            enddate = request.POST.get('enddate')
            cursor.execute(f'insert into restaurant_promo values (\'{rname}\', \'{rbranch}\', \'{pid}\', \'{startdate}\', \'{enddate}\')')
            connection.commit()
            return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo_restoran', kwargs={'rname':rname, 'rbranch':rbranch}))

        except Exception as e:
            connection.rollback()
            context = {
                'message':e.args[0:40],
                'role':request.COOKIES.get('role'),
                'rname':rname,
                'rbranch':rbranch,
                'record_promoname':record_promoname,
            }
            return render(request, 'form_promo_restoran.html', context)

    context =  {
        'role':request.COOKIES.get('role'),
        'rname':rname,
        'rbranch':rbranch,
        'record_promoname':record_promoname,
    }
    return render(request, 'form_promo_restoran.html', context)

def show_form_ubah_promo_restoran(request, id):
    cursor.execute(f'select promoname, discount from promo where id = \'{id}\'')
    record_pname = cursor.fetchall()

    cursor.execute(f'select count(*) from special_day_promo where id = \'{id}\'')
    record_count = cursor.fetchall()
    if int(record_count[0][0])  > 0:
        jenis = 'Promo Hari Spesial'
    else:
        jenis = 'Promo Minimum Transaksi' 

    if request.method == 'POST':
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        rname = request.COOKIES.get('rname')
        rbranch = request.COOKIES.get('rbranch')

        if start_date == '' or end_date == '':
            context = {
                'jenis_promo':jenis,
                'nama_promo':record_pname[0][0],
                'status':'error',
                'message':'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu',
                'role':request.COOKIES.get('role'),
                'rname':request.COOKIES.get('rname'),
                'rbranch':request.COOKIES.get('rbranch'),
                'discount':record_pname[0][1],
            }
            return render(request, 'form_ubah_promo_restoran.html', context)
        else:
            try:
                cursor.execute(f'update restaurant_promo set startdate = \'{start_date}\', enddate = \'{end_date}\' where rname = \'{rname}\' and rbranch = \'{rbranch}\' and pid = \'{id}\'')
                connection.commit()
                return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo_restoran', kwargs={'rname':rname, 'rbranch':rbranch}))

            except Exception as e:
                connection.rollback()
                context = {
                    'jenis_promo':jenis,
                    'nama_promo':record_pname[0][0],
                    'status':'error',
                    'message':e.args[0][:40],
                    'role':request.COOKIES.get('role'),
                    'rname':request.COOKIES.get('rname'),
                    'rbranch':request.COOKIES.get('rbranch'),
                    'discount':record_pname[0][1],
                }
                return render(request, 'form_ubah_promo_restoran.html', context)

    context = {
        'jenis_promo':jenis,
        'nama_promo':record_pname[0][0],
        'discount':record_pname[0][1],
        'role':request.COOKIES.get('role'),
        'rname':request.COOKIES.get('rname'),
        'rbranch':request.COOKIES.get('rbranch'),
    }

    return render(request, 'form_ubah_promo_restoran.html', context)

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
    
    context = {
        'records_promo':records_promo[0],
        'role':request.COOKIES.get('role'),
        'rname':request.COOKIES.get('rname'),
        'rbranch':request.COOKIES.get('rbranch'),
    }

    return render(request, 'detail_promosi.html', context)

def show_detail_promo_restoran(request, rname, rbranch, id):
    cursor.execute(f'select * from promo p, restaurant_promo r where p.id = r.pid and r.pid = \'{id}\' and r.rname = \'{rname}\' and r.rbranch = \'{rbranch}\'')
    record_promo = cursor.fetchall()

    cursor.execute(f'select * from special_day_promo where id = \'{id}\'')
    record = cursor.fetchmany()
    if len(record) == 1:
        record_promo[0] += ('Promo Hari Spesial',)

    cursor.execute(f'select * from min_transaction_promo where id = \'{id}\'')
    record = cursor.fetchmany()
    if len(record) == 1:
        record_promo[0] += ('Promo Minimum Transaksi',)

    record_promo = list(record_promo[0])
    record_promo[6] = record_promo[6].date()
    record_promo[7] = record_promo[7].date()
    context = {
        'record_promo':record_promo,
        'id':id,
        'rname':rname,
        'rbranch':rbranch,
    }

    print(record_promo)
    return render(request, 'detail_promosi_restoran.html', context)

def delete_promo(request, id):
    cursor.execute(f'delete from promo where id = \'{id}\'')
    connection.commit()
    return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo'))

def delete_promo_restoran(request, rname, rbranch, id):
    cursor.execute(f'delete from restaurant_promo where pid = \'{id}\' and rname = \'{rname}\' and rbranch = \'{rbranch}\'')
    connection.commit()
    return HttpResponseRedirect(reverse('trigger_6:show_daftar_promo_restoran'))

def ubah_form_input(request, id):
    cursor.execute(f'select discount from sirest.promo where id = \'{id}\'')
    discount = cursor.fetchone()
    
    cursor.execute(f'select id from sirest.special_day_promo')
    special_day_promo_id = cursor.fetchall()

    if (str(id),) in special_day_promo_id:
        jenis_promo = 'Promo Hari Spesial'
        cursor.execute(f'select date from sirest.special_day_promo where id = \'{id}\'')
        special_date = cursor.fetchone()
        context = {
            'discount':discount[0],
            'jenis_promo':jenis_promo,
            'special_date':special_date[0],
        }
    else:
        jenis_promo = 'Promo Minimum Transaksi'
        cursor.execute(f'select minimumtransactionnum from sirest.min_transaction_promo where id = \'{id}\'')
        min_transaction = cursor.fetchone()

        context = {
            'discount':discount[0],
            'jenis_promo':jenis_promo,
            'min_transaction':min_transaction,
        }

    return JsonResponse(context)