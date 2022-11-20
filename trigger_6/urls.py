from django.urls import path
from trigger_6.views import *

app_name = 'trigger_6'

urlpatterns = [
    path('', show_riwayat, name='show_riwayat'),
]