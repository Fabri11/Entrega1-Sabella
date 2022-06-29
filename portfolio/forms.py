from django import forms

class FormularioPortafolio(forms.Form):
    proyecto = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=250)
    url = forms.URLField(max_length=350)