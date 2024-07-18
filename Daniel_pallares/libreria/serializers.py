from libreria.models import Usuario,Libro,Autor,Prestamo
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'username', 'email', 'groups','nombre','apellido']


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

    def validate(self, data):
        if data['numero_paginas'] < 0:
            raise serializers.ValidationError('no libros con paginas = 0')
        return data

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
    
    def validate(self, data):
        prestamos =Prestamo.objects.filter(libro__titulo=str(data['libro']) ,fecha_devolucion__isnull=True)
        if len(prestamos) >0:
            raise serializers.ValidationError('no se puede prestar un libro dos veces')
        return data