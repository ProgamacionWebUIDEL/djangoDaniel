from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=120, help_text='pagina principal')
    autor = models.CharField(max_length=120, help_text='pagina principal')
    numero_paginas = models.IntegerField(max_length= 1000,help_text='numero de paginas')
    editorial = models.CharField(max_length=120,help_text='editorial del libro')

class Autos(models.Model):
    marca = models.CharField(max_length=200,help_text='Ingrese la marca del vehiculo')
    cilindraje = models.FloatField(help_text= 'Ingrese el cilindraje')
    
class Computadoras(models.Model):
    marca = models.CharField(max_length= 200,help_text='Ingrese la marca de la computadora')
    precio = models.IntegerField(max_length=200,help_text='Ingrese el precio de la computadora')
    codigo = models.IntegerField(max_length=200,help_text='Ingrese el codigo de la computadora')
