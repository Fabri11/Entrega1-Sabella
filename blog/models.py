
from django.db import models
import datetime

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog/imagenes')
    data = models.DateField(datetime.date.today)