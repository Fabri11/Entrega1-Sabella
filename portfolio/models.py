from distutils.command import upload
from tokenize import blank_re
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Create your models here.


class Project(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to = "portfolio/imagenes/")
    url = URLField(blank=True)

