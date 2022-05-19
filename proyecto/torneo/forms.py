from django import forms

class JugadoresFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    equipo = forms.CharField(max_length=40)

class EquiposFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=1)

class SedesFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)