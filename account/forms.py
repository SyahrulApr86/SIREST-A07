from django import forms
from utils.query import *

cursor.execute("select distinct province from delivery_fee_per_km")
records = cursor.fetchall()
DATA_PROVINSI = []
for record in records:
    DATA_PROVINSI.append((record[0], record[0]))

cursor.execute("select id, name from restaurant_category")
records = cursor.fetchall()
DATA_KATEGORI = []
for record in records:
    DATA_KATEGORI.append((record[0], record[1]))

class RegisterFormAdmin(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))


class RegisterFormPelanggan(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    # tanggal lahir date picker
    tanggal_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput({
                                    'class': 'form-control', 'type': 'date'}))
    # jenis kelamin dropdown
    jenis_kelamin = forms.ChoiceField(label='Jenis Kelamin', choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Jenis Kelamin', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))


class RegisterFormRestoran(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))

    nama_restoran = forms.CharField(label='Nama Restoran', max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Restoran', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    cabang = forms.CharField(label='Cabang', max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Cabang', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    no_hp_restoran = forms.CharField(label='No Telepon Restoran', max_length=18, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Telepon Restoran'}))
    jalan = forms.CharField(label='Jalan', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Jalan', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    kecamatan = forms.CharField(label='Kecamatan', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Kecamatan', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    kota = forms.CharField(label='Kota', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Kota', 'oninvalid': "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput': "setCustomValidity('')"}))
    # provinsi dropdown
    provinsi = forms.ChoiceField(label='Provinsi', choices=DATA_PROVINSI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2l', 'placeholder': 'Provinsi', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    # kategori dropdown
    kategori = forms.ChoiceField(label='Kategori', choices=DATA_KATEGORI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Kategori', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))


class RegisterFormKurir(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))

    plat_no_kendaraan = forms.CharField(label='Plat No Kendaraan', max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Plat No Kendaraan', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    no_sim = forms.CharField(label='No SIM', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No SIM', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    # Jenis Kendaraan Dropdown
    jenis_kendaraan = forms.ChoiceField(label='Jenis Kendaraan', choices=[('Car', 'Mobil'), ('Motorcycle', 'Motor')], widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Jenis Kendaraan', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
    merk_kendaraan = forms.CharField(label='Merk Kendaraan', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Merk Kendaraan', 'oninvalid' : "this.setCustomValidity('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')", 'oninput' : "setCustomValidity('')"}))
