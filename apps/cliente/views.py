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
    cuenta = filtro_cuenta.filter(account_id=filtro_cuenta[0].account_id)
    balance_final = cuenta[0].balance 
    cuenta.update(balance=balance_final)
    
    return render(request,'cliente/index.html',{'balance':balance_final})