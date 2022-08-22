from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  
# Create your views here.  
  
def registro(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = CustomUserCreationForm()  
        context = {'form':form}  
    return render(request, 'registro/registro.html', context)  