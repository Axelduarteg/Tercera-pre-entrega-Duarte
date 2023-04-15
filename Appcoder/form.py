from django import forms

class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)
    
class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    
class EntregableForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()
    
class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()
    
class EntregableForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()