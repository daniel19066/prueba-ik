from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    class YearInSchool(models.TextChoices):
        Colombia = 'CO', _('Colombia')
        Ecuador = 'EC', _('Ecuador')
        Venezuela = 'VE', _('Venezuela')

    pais = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.Colombia,
    )
    fecha_fallecimiento = models.DateField(max_length=100, blank=True,null=True)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    numero_paginas = models.PositiveIntegerField()
    editorial = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13,unique=True)  

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)  # Opcional

    def __str__(self):
        return f"Prestamo de '{self.libro.titulo}' a '{self.usuario.username}'"