"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.ZZZApi.views import AuthUserList

urlpatterns = [
 path('admin/', admin.site.urls),
 path('cliente/', include ('apps.cliente.urls'), name='cliente'),
 path('cuenta/', include ('apps.cuenta.urls'), name='cuenta'),
 path('tarjeta/', include ('apps.tarjeta.urls'), name='tarjeta'),
 path('prestamo/', include ('apps.prestamo.urls'), name='prestamo'),
 path('registro/', include ('apps.registro.urls'), name='registro'),
 path('', include ('apps.home.urls'), name='home'),
 path('ZZZApi/', include('apps.ZZZApi.urls'), name = 'ZZZApi'),
 path('Cliente/', include('apps.ApiDatosCliente.urls'), name = 'Cliente'),
 ]