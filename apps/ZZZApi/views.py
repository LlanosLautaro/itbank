
from .models import AuthUser
from .serializers import AuthUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AuthUserDetails(APIView):
    def get(self, request, pk):
        User = AuthUser.objects.filter(pk=pk).first()
        serializer = AuthUserSerializer(User)
        if User:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)





class AuthUserList(APIView):
    
    def get(self, request): # nuevo
        Usuarios = AuthUser.objects.all().order_by('created_at')
        serializer = AuthUserSerializer(Usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
"""     http_method_names = ['get', 'head']
    
    def get(self, request, format=None):
        ausers = AuthUser.objects.all()
        serializer = AuthUserSerializer(ausers, many=True)
        return Response(serializer.data)
 """



