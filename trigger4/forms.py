from django import forms

DATA_PROVINSI = [('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('Jawa Timur', 'Jawa Timur'),
             ('DKI Jakarta', 'DKI Jakarta')]

class FormBuatKategoriMakanan(forms.Form):
        nama = forms.CharField(label='Nama Kategori Makanan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

class FormPengisianAlamatMakanan(forms.Form):
        Jalan = forms.CharField(label='Jalan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

        Kecamatan = forms.CharField(label='Kecamatan', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

        Kota= forms.CharField(label='Kota', max_length=100, widget=forms.TextInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'label'}))

        Provinsi = forms.ChoiceField(label='Provinsi', choices=DATA_PROVINSI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Hari'}))