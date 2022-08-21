from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index_tarjetas(request):
    return render(request,'tarjetas/index.html')