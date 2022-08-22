from venv import create
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.cliente.models import Cliente
from apps.cuenta.models import Cuenta
from .models import Prestamo
from .forms import PrestamoForm


# Create your views here.
@login_required

def index_prestamos(request):
    return render(request, 'prestamos/index.html')


def solicitarPrestamo(request):

    usuario = Cliente.objects.get(customer_name = User.get_username(request.user))
    tipo_cliente = usuario.customer_type_id
    customerID = usuario.customer_id
    form = PrestamoForm()

    filtro_cuenta = Cuenta.objects.filter(customer_id=customerID)
    cuenta = filtro_cuenta.filter(account_id=filtro_cuenta[0].account_id)

    match tipo_cliente:
        case 3:
            prestamo_max = 500000
        case 2:
            prestamo_max = 300000
        case 1:
            prestamo_max = 100000

    if request.method == 'POST':
        form = PrestamoForm(request.POST)

        if form.is_valid():

            prestamo = Prestamo()
            prestamo.loan_type = form.cleaned_data['loan_type']
            prestamo.loan_date = form.cleaned_data['loan_date']
            prestamo.loan_total = form.cleaned_data['loan_total']
            loan_total = prestamo.loan_total
            loan_type = prestamo.loan_type
            loan_date = prestamo.loan_date

            if loan_total >= prestamo_max:
                return render(request, 'prestamos/prestamo_denegado.html', {'form': form, })

            else:
                balance_final = cuenta[0].balance + loan_total
                cuenta.update(balance=balance_final)
                Prestamo.objects.create(
                    loan_total=loan_total,
                    loan_date=loan_date,
                    loan_type=loan_type, 
                    customer_id = customerID)
                return render(request, 'prestamos/prestamo_exitoso.html', {'form': form},)
            

    return render(request, 'prestamos/solicitud.html', {'form': form},)
# 'error':True
# ,'success':True