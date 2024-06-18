from django.contrib import admin
from pelicula.models import Pelicula, User

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(User)