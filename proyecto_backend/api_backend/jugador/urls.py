from django.urls import path
from jugador import views

urlpatterns = [
    path ('index_jugadores/', views.index_jugadores, name= 'index_jugadores'),
    path('jugadores_rest/', views.jugadores_rest, name= 'jugadores_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    # path('add_jugadores/', views.get_all_jugadores, name='get_all_jugadores'),
    path ('new_jugador/', views.NewJugadorView.as_view(), name= 'new_jugador'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
    
]
