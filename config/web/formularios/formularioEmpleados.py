from django import forms

class FormularioEmpleados(forms.Form):
    OPCIONES = (
        (1,'Administrador'),
        (2, 'Empleados'),
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT
    nombresEmpleados = forms.CharField(
        widget = forms.TextInput(attrs = {'class':'form-control mb-3'}),
        required = True,
        max_length = 50
    )

    apellidosEmpleados = forms.CharField(
        widget = forms.TextInput(attrs = {'class':'form-control mb-3'}),
        required = True,
        max_length = 50
    )

    fotoEmpleados = forms.CharField(
        widget = forms.TextInput(attrs = {'class':'form-control mb-3'}),
        required = True,
        max_length = 200,
    )

    cargoEmpleados = forms.ChoiceField(
        widget = forms.Select(attrs = {'class':'form-control mb-3'}),
        required = True,
        choices = OPCIONES,
    )
    
    salarioEmpleados = forms.CharField(
        widget = forms.NumberInput(attrs = {'class':'form-control mb-3'}),
        required = True,
    )

    contactoEmpleados = forms.CharField(
        widget = forms.TextInput(attrs = {'class':'form-control mb-3'}),
        required = True,
        max_length = 20
    )