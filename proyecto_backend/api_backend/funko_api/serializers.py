from rest_framework import serializers

from funko_api.models import Funko


class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'
        
