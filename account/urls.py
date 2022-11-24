from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register_admin/', register_admin, name='register_admin'),
    path('register_pelanggan/', register_pelanggan, name='register_pelanggan'),
    path('register_restoran/', register_restoran, name='register_restoran'),
    path('register_kurir/', register_kurir, name='register_kurir'),
    path('dashboard_admin/',dashboard_admin,name='dashboard-admin'),
    path('profile_restoran/',profile_restoran,name='profile_restoran'),
    path('profile_pelanggan/',profile_pelanggan,name='profile_pelanggan'),
    path('profile_kurir/',profile_kurir,name='profile_kurir'),
]