
from .models import AuthUser
from .serializers import AuthUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class AuthUserList(APIView):
    
    
    
    http_method_names = ['get', 'head']
    
    def get(self, request, format=None):
        ausers = AuthUser.objects.all()
        serializer = AuthUserSerializer(ausers, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    




