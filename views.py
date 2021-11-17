from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializable,AutoSerializable,ComputadoraSerializable
from .models import Libro
from .models import Autos
from .models import Computadoras

# Create your views here.
class LibroVista (viewsets.ModelViewSet):
    serializer_class:LibroSerializable
    queryset = Libro.objects.all()

class AutosVista (viewsets.ModelViewSet):
    serializer_class:AutoSerializable
    queryset = Autos.objects.all()

class ComputadorasVista (viewsets.ModelViewSet):
    serializer_class:ComputadoraSerializable
    queryset = Computadoras.objects.all()
