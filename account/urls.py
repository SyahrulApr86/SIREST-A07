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
]