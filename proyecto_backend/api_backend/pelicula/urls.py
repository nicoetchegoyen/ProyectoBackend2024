from django.urls import path
from pelicula import views

urlpatterns = [
    path ('index_pelicula/', views.index_pelicula, name= 'index_pelicula'),
    path('pelicula_rest/', views.pelicula_rest, name= 'pelicula_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    # path('add_jugadores/', views.get_all_jugadores, name='get_all_jugadores'),
    path ('new_pelicula/', views.NewPeliculaView.as_view(), name= 'new_pelicula'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
    
]
