from django.shortcuts import render
from .models import Cliente
from .serializers import ClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ClienteDetalles(APIView):
    def get(self, request, pk):
        User = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(User)
        if User:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

