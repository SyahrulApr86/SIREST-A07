from django import forms

DATA_HARI = [('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'),
             ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')]


class FormIsiSaldo(forms.Form):
    saldo_pengisian = forms.IntegerField(label='Nominal Pengisian', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nominal'}))


class FormTarikSaldo(forms.Form):
    saldo_penarikan = forms.IntegerField(label='Nominal Penarikan', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nominal'}))


class FormBuatJamOperasional(forms.Form):
    # Hari dropdown
    hari = forms.ChoiceField(label='Hari', choices=DATA_HARI, widget=forms.Select(
        attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mt-2', 'placeholder': 'Hari'}))

    # Jam buka time picker
    jam_buka = forms.TimeField(label='Jam Buka', widget=forms.TimeInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'time'}))

    # Jam tutup time picker
    jam_tutup = forms.TimeField(label='Jam Tutup', widget=forms.TimeInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'time'}))


class FormEditJamOperasional(forms.Form):
    # Jam buka time picker
    jam_buka = forms.TimeField(label='Jam Buka', widget=forms.TimeInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'time'}))

    # Jam tutup time picker
    jam_tutup = forms.TimeField(label='Jam Tutup', widget=forms.TimeInput(
        attrs={'class': 'w-[20rem] h-[2.5rem] rounded-lg border-2 border-gray-300', 'type': 'time'}))