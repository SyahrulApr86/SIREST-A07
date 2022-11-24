from django.shortcuts import render

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
    return render(request, 'daftar_promo.html')

def show_ubah_promo(request):
    return render(request, 'form_ubah_promosi.html')

def show_daftar_promo_restoran(request):
    return render(request, 'daftar_promo_restoran.html')

def show_form_promo_restoran(request):
    return render(request, 'form_promo_restoran.html')

def show_form_ubah_promo_restoran(request):
    return render(request, 'form_ubah_promo_restoran.html')