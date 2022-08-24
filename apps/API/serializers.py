from rest_framework import serializers
from .models import AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        #indicamos que use todos los campos
        fields = "__all__"
#les decimos cuales son los de solo lectura
#read_only_fields = ("id","created_at","updated_at",)





    


""" class AuthUser(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=255)
    last_login = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    is_staff = serializers.CharField(max_length=255)
    is_active = serializers.CharField(max_length=255)
    date_joined = serializers.DateTimeField(read_only=True)
    clave = serializers.CharField(max_length=255)
    telefono = serializers.CharField(max_length=255)
    customer_id = serializers.CharField(max_length=255) """









    