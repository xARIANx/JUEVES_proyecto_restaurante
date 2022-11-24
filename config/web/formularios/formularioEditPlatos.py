from django import forms

class FormularioEditPlatos(forms.Form):

    precioPlato = forms.CharField(
        widget = forms.NumberInput(attrs = {'class':'form-control mb-3'}),
        required = True,
    )