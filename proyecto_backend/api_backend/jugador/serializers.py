from rest_framework import serializers

from jugador.models import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['nombre',
                  'club',
                  'pais',
                  'retirado',]
        