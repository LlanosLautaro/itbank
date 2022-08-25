from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
class ClienteDetalles(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


