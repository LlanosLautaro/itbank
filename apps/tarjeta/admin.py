from django.contrib import admin
from apps.tarjeta.models import MarcaTarjeta,Tarjeta,TipoCliente
# Register your models here.
admin.site.register(MarcaTarjeta)
admin.site.register(Tarjeta)
admin.site.register(TipoCliente)