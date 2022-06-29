from django import forms
import datetime

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.TextInput()
    imagen = forms.ImageField()
    data = forms.DateField()