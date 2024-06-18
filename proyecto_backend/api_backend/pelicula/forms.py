from django import forms

from pelicula.models import Pelicula, User

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = [
            'nombre',
            'director',
            'anio',
            'oscar',
        ]
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'peliculas',
        ]
        