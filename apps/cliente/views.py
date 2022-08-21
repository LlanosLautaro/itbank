from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index_clientes(request):
    return render(request,'cliente/index.html')