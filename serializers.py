from enum import auto
from django.db.models import fields
from rest_framework import serializers
from .models import Libro
from .models import Autos
from .models import Computadoras


class LibroSerializable(serializers.ModelSerializer):
    class Meta:
        model = Libro 
        fields =(
            'titulo',
            'autor'
            'numero_paginas'
            'editorial'
        )
class AutoSerializable(serializers.ModelSerializer):
    class Meta:
        model = Autos
        fields =(
            'marca',
            'cilindraje'
        )
class ComputadoraSerializable(serializers.ModelSerializer):
    class Meta:
        model = Computadoras
        fields =(
            'marca',
            'precio'
        )