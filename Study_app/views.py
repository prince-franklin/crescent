from django.shortcuts import render, redirect
from django.http import HttpResponse
from Study_app.form import crescentForm
from Study_app.models import Crescentlib
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def crescent(request):
    if request.method=="POST":
        form=crescentForm(request.POST or None )
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manager=request.user
            instance.save()
        messages.success(request, ('Added succesfully'))
        return redirect('crescent')
    else:
        resources= Crescentlib.objects.filter(manager=request.user)
        paginator=Paginator(resources,10)
        page=request.GET.get('pg')
        resources=paginator.get_page(page)
        return render(request, 'crescent.html' , {'resources' : resources})

def manuscripts(request):
    return render(request, 'manuscripts.html')

def periodicals(request):
    return render(request, 'periodicals.html')

def science(request):
    return render(request, 'science.html')

def software(request):
    return render(request, 'software.html')

def index(request):
    return render(request, 'index.html')

def delete_task(request, task_id):
    task=Crescentlib.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request, ('Access Restricted'))

    return redirect('crescent')

def completed (request, task_id):
    task=Crescentlib.objects.get(pk=task_id)
    if task.manager == request.user:
        task.read=True
        task.save()
    else:
        messages.error(request, ('Access Restricted'))
    return redirect('crescent')


def pending (request, task_id):
    task=Crescentlib.objects.get(pk=task_id)
    if task.manager == request.user:
        task.read=False
        task.save()
    else:
         messages.error(request, ('Access Restricted'))
    return redirect('crescent')


def edit_task(request, task_id):
    if request.method=="POST":
        resources=Crescentlib.objects.get(pk=task_id)
        form=crescentForm(request.POST or None, instance= resources )
        form.is_valid()
        form.save()
        messages.success(request, ('Updated Successfully'))
        return redirect('crescent')
    else:
        resources_up= Crescentlib.objects.get(pk=task_id)
        return render(request, 'edit.html' , {'resources_up' : resources_up})
