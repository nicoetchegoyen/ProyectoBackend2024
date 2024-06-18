from django import forms

from jugador.models import Jugador, User

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            'nombre',
            'club',
            'pais',
            'retirado',
        ]
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'jugadores',
        ]
        
