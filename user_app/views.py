from django.shortcuts import render, redirect
from django.contrib import messages
from .form import AdditionForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def register(request):
    if request.method=="POST":
        register_form=AdditionForm(request.POST)
        register_form.save()
        messages.success(request, ('New user created succesfully'))
        return redirect('register')
    else:
        register_form=AdditionForm()
        return render(request, 'register.html', {'register_form': register_form})
    
def custom_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('crescent')
        else:
            messages.info(request, 'Wrong Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')
            
    
    