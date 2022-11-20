from django import forms


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
    tanggal_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput({'class': 'form-control', 'type': 'date'}))
    # jenis kelamin dropdown
    jenis_kelamin = forms.ChoiceField(label='Jenis Kelamin', choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Jenis Kelamin'}))
