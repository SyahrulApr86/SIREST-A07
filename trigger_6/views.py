from django.shortcuts import render

# Create your views here.
def show_riwayat(request):
    return render(request, 'riwayat.html')
