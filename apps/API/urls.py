from django.urls import path
from .views import AuthUserList

urlpatterns = [
    path('', AuthUserList.as_view(), name= 'API'), 
     ]