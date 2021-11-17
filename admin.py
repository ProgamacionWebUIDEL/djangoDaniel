from django.contrib import admin
from .models import Libro
from .models import Autos
from .models import Computadoras
# Register your models here.
admin.site.register(Libro)
admin.site.register(Autos)
admin.site.register(Computadoras)