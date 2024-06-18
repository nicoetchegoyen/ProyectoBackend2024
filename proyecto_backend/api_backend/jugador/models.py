from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=128)
    club = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)
    retirado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.club} - {self.nombre}'

class User(models.Model):
    name = models.CharField(max_length=128)
    jugadores = models.ManyToManyField(Jugador, blank=True)

    def __str__(self):
        return self.name