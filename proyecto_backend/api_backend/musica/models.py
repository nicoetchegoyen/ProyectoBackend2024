
from django.db import models

# Create your models here.
class Musica(models.Model):
    cancion = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)
    album = models.CharField(max_length=128)

    
    def __str__(self):
        return f'{self.cancion} - {self.album}'

class User(models.Model):
    name = models.CharField(max_length=128)
    musica = models.ManyToManyField(Musica, blank=True)

    def __str__(self):
        return self.name

