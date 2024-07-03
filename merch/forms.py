from django import forms

class ProductosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required= True)
    codigo = forms.CharField(required=True)
    precio = forms.FloatField(required=True)
    fabricante = forms.CharField(max_length=50, required=True)


class DVDForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    codigo = forms.IntegerField(required=True)
    precio = forms.FloatField(required=True)
    tipo = forms.BooleanField(required=True)
    en_stock = forms.BooleanField(required=True)

class DistribuidorForm(forms.Form):
    empresa = forms.CharField(max_length=50,required=True)
    repartidor = forms.CharField(max_length=50,required=True)
    apellido = forms.CharField(max_length=50,required=True)
    edad = forms.IntegerField(required=True)

