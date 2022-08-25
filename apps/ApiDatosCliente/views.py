from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


class ClienteDetalles(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def cliente_de_usuario(self, request):
        cliente = Cliente.objects.get(pk = request.user.cliente.customer_id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
