from django.urls import path
from .views import AuthUserList
from .views import AuthUserDetails

urlpatterns = [
    path('<int:pk>/',AuthUserDetails.as_view()),
    #path('', AuthUserList.as_view(), name= 'API'), 
     ]