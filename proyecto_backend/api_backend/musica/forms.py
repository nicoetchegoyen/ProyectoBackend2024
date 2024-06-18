from django import forms

from musica.models import Musica, User

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = [
            'cancion',
            'autor',
            'album',
            
        ]
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'musica',
        ]
        