from django.urls import path
#Se importan todas las vistas del proyecto
from . import views

urlpatterns = [
 path('', views.index_prestamos, name='index_prestamos'),
 path('solicitar-prestamo/',views.solicitarPrestamo, name='solicitarPrestamo')
]