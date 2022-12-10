from django import forms

# dummy data (masih hard coded)
DATA_PROVINSI = [('Jabar', 'Jawa Barat'), ('Jatim', 'Jawa Timur')]
DATA_KATEGORI = [('3', 'Cafe'), ('Fast Food', 'Fast Food')]

class RegisterFormAdmin(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********'}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP'}))


class RegisterFormPelanggan(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********'}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP'}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK'}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank'}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening'}))
    # tanggal lahir date picker
    tanggal_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput({
                                    'class': 'form-control', 'type': 'date'}))
    # jenis kelamin dropdown
    jenis_kelamin = forms.ChoiceField(label='Jenis Kelamin', choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Jenis Kelamin'}))


class RegisterFormRestoran(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********'}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP'}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK'}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank'}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening'}))

    nama_restoran = forms.CharField(label='Nama Restoran', max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Restoran'}))
    cabang = forms.CharField(label='Cabang', max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Cabang'}))
    no_hp_restoran = forms.CharField(label='No Telepon Restoran', max_length=18, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Telepon Restoran'}))
    jalan = forms.CharField(label='Jalan', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Jalan'}))
    kecamatan = forms.CharField(label='Kecamatan', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Kecamatan'}))
    kota = forms.CharField(label='Kota', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Kota'}))
    # provinsi dropdown
    provinsi = forms.ChoiceField(label='Provinsi', choices=DATA_PROVINSI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2l', 'placeholder': 'Provinsi'}))
    # kategori dropdown
    kategori = forms.ChoiceField(label='Kategori', choices=DATA_KATEGORI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Kategori'}))


class RegisterFormKurir(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '***********'}))
    nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    no_hp = forms.CharField(label='No HP', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No HP'}))
    nik = forms.CharField(label='NIK', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'NIK'}))
    nama_bank = forms.CharField(label='Nama Bank', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Bank'}))
    no_rekening = forms.CharField(label='No Rekening', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No Rekening'}))

    plat_no_kendaraan = forms.CharField(label='Plat No Kendaraan', max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Plat No Kendaraan'}))
    no_sim = forms.CharField(label='No SIM', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'No SIM'}))
    # Jenis Kendaraan Dropdown
    jenis_kendaraan = forms.ChoiceField(label='Jenis Kendaraan', choices=[('Car', 'Mobil'), ('Motorcycle', 'Motor')], widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Jenis Kendaraan'}))
    merk_kendaraan = forms.CharField(label='Merk Kendaraan', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Merk Kendaraan'}))
