from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required

def index_clientes(request):
    return render(request,'cliente/index.html')