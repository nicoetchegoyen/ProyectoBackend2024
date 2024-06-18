from django.http import JsonResponse
from django.shortcuts import render
from musica.models import Musica
from musica.serializers import MusicaSerializer
from musica.forms import MusicaForm, UserForm
from django.views.generic import CreateView

# Create your views here.


def get_all_musica():
    musica = Musica.objects.all().order_by('album')
    musica_serializers = MusicaSerializer(musica, many=True)
    return musica_serializers.data

def index_musica(request):
    musica = get_all_musica()
    return render(request, 'index_musica.html', {'musica': musica})

def musica_rest(request):
    musica  = get_all_musica()
    return JsonResponse(musica, safe=False)

def users_rest(request):
    return JsonResponse("Ok", safe=False)

class NewMusicaView(CreateView):
    form_class = MusicaForm
    template_name = 'form_musica.html'
    success_url = '/index_musica/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_musica.html'
    success_url = '/'
