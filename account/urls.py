from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('register_admin/', register_admin, name='register_admin'),
    path('register_pelanggan/', register_pelanggan, name='register_pelanggan'),
    path('register_restoran/', register_restoran, name='register_restoran'),
    path('register_kurir/', register_kurir, name='register_kurir'),
    path('dashboard_admin/', dashboard_admin, name='dashboard-admin'),
    path('profile_restoran/<email>', profile_restoran, name='profile_restoran'),
    path('profile_pelanggan/<email>', profile_pelanggan, name='profile_pelanggan'),
    path('profile_kurir/<email>', profile_kurir, name='profile_kurir'),
    path('verifikasi_user/<email_user>/<email_admin>',
         verifikasi_user, name='verifikasi_user'),
]
