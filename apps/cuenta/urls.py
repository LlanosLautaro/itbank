from django.urls import path
#Se importan todas las vistas del proyecto
from . import views

urlpatterns = [
 path('', views.index_cuentas, name='index_cuentas'),
]