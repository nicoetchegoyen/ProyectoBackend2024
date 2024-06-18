from django.http import JsonResponse
from django.shortcuts import render
from pelicula.models import Pelicula
from pelicula.serializers import PeliculaSerializer
from pelicula.forms import PeliculaForm, UserForm
from django.views.generic import CreateView

# Create your views here.


def get_all_peliculas():
    peliculas = Pelicula.objects.all().order_by('anio')
    peliculas_serializers = PeliculaSerializer(peliculas, many=True)
    return peliculas_serializers.data

def index_pelicula(request):
    peliculas = get_all_peliculas()
    return render(request, 'index_pelicula.html', {'peliculas': peliculas})

def pelicula_rest(request):
    peliculas  = get_all_peliculas()
    return JsonResponse(peliculas, safe=False)

def users_rest(request):
    return JsonResponse("Ok", safe=False)

class NewPeliculaView(CreateView):
    form_class = PeliculaForm
    template_name = 'form_pelicula.html'
    success_url = '/index_pelicula/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_pelicula.html'
    success_url = '/'


