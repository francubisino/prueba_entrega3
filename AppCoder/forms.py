from django import forms

class SucursalesFormulario(forms.Form):
    ubicacion=forms.CharField()
    numero=forms.IntegerField()
    nombre_encargado=forms.CharField()

class ConsultasFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()    
    consulta=forms.CharField()

class ProductosFormulario(forms.Form):
    nombre=forms.CharField()
    
class InicioFormulario(forms.Form):
    pais_origen=forms.CharField()
    
    