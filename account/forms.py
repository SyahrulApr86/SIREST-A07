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
