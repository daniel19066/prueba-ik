from django.shortcuts import render
from rest_framework import permissions, viewsets
from libreria.models import Prestamo,Autor,Usuario,Libro
from libreria.serializers import AutorSerializer,LibroSerializer,PrestamoSerializer,UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]

class PrestamoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    #permission_classes = [permissions.IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    #permission_classes = [permissions.IsAuthenticated]

class LibroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    #permission_classes = [permissions.IsAuthenticated]
