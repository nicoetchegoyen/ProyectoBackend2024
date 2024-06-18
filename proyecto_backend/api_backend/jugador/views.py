from django.http import JsonResponse
from django.shortcuts import render
from jugador.models import Jugador
from jugador.serializers import JugadorSerializer
from jugador.forms import JugadorForm, UserForm
from django.views.generic import CreateView

# Create your views here.


def get_all_jugadores():
    jugadores = Jugador.objects.all().order_by('club')
    jugadores_serializers = JugadorSerializer(jugadores, many=True)
    return jugadores_serializers.data

def index_jugadores(request):
    jugadores = get_all_jugadores()
    return render(request, 'index_jugadores.html', {'jugadores': jugadores})

def jugadores_rest(request):
    jugadores  = get_all_jugadores()
    return JsonResponse(jugadores, safe=False)

def users_rest(request):
    return JsonResponse("Ok", safe=False)

class NewJugadorView(CreateView):
    form_class = JugadorForm
    template_name = 'form_jugador.html'
    success_url = '/index_jugadores/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_jugador.html'
    success_url = '/'

