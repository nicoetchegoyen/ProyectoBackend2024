from rest_framework import serializers

from musica.models import Musica

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = ['cancion',
                  'autor',
                  'album',
                  ]