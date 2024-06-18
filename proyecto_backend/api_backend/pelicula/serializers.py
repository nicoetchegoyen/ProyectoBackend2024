from rest_framework import serializers

from pelicula.models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ['nombre',
                  'director',
                  'anio',
                  'oscar',]