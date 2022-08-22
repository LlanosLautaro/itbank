from django.shortcuts import render
from apps.cuenta.models import Cuenta
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
@login_required

def index_clientes(request):

    usuario = Cliente.objects.get(customer_name = User.get_username(request.user))
    
    customerID = usuario.customer_id
    filtro_cuenta = Cuenta.objects.filter(customer_id=customerID)
    filtro_cliente = Cliente.objects.filter(customer_id=customerID)
    cuenta = filtro_cuenta.filter(account_id=filtro_cuenta[0].account_id)
    balance_final = cuenta[0].balance 
    clase= cuenta[0].account_type
    cliente =filtro_cliente.filter(customer_id=filtro_cliente[0].customer_id)
    tipo_cliente = cliente[0].customer_type
    cuenta.update(balance=balance_final)
    
    return render(request,'cliente/index.html',{'balance':balance_final, 'clase':clase,'tipo_cliente':tipo_cliente})