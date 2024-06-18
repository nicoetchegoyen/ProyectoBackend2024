from django.urls import path
from musica import views

urlpatterns = [
    path ('index_musica/', views.index_musica, name= 'index_musica'),
    path('musica_rest/', views.musica_rest, name= 'musica_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    # path('add_jugadores/', views.get_all_jugadores, name='get_all_jugadores'),
    path ('new_musica/', views.NewMusicaView.as_view(), name= 'new_musica'),
    path('new_user/', views.NewUserView.as_view(), name='new_user'),
    
]
