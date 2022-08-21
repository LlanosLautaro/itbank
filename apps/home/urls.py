from django.urls import path
#Se importan todas las vistas del proyecto
from . import views

urlpatterns = [
 path('', views.home, name='home'),
]