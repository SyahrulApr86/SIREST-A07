from django import forms
from utils.query import *

cursor.execute("select distinct province from delivery_fee_per_km")
records = cursor.fetchall()
DATA_PROVINSI = []
for record in records:
    DATA_PROVINSI.append((record[0], record[0]))

DATA_KENDARAAN = [('Mobil', 'Mobil'), ('Motor', 'Motor')]


class FormBuatKategoriMakanan(forms.Form):
    nama = forms.CharField(label='Nama Kategori Makanan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))


# class FormPemilihanPesananPadaRestoran(forms.Form):
#     hari = forms.ChoiceField(label='Hari', choices=DATA_HARI, widget=forms.Select(
#         attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Hari'}))


class FormPengisianAlamatMakanan(forms.Form):
    Jalan = forms.CharField(label='Jalan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

    Kecamatan = forms.CharField(label='Kecamatan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

    Kota = forms.CharField(label='Kota', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

    # Provinsi = forms.ChoiceField(label='Provinsi', choices=DATA_PROVINSI, widget=forms.Select(
    # attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Hari'}))
     