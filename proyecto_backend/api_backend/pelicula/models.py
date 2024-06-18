from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    anio = models.CharField(max_length=128)
    oscar = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.anio} - {self.nombre}'

class User(models.Model):
    name = models.CharField(max_length=128)
    peliculas = models.ManyToManyField(Pelicula, blank=True)

    def __str__(self):
        return self.name
