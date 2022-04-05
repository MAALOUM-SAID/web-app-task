
from django.shortcuts import redirect, render

from .form import *
from .models import Task

# Create your views here.

def index(request):
    task=Task.objects.all()
    return render(request,'pages/index.html',{'task':task})
def users(request):
    task_Form=TaskForm()
    if request.method=='POST':
        task_Form=TaskForm(request.POST)
        if task_Form.is_valid():
            task_Form.save()
            return redirect(to='index')
    context={
        'task':task_Form
    }
    return render(request,'pages/users.html',context)
def update(request,pk):
    task=Task.objects.get(id=pk)    
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect(to='index')
    context={
        'form':form,
    }
    return render(request,'pages/update.html',context)

def delete(request,pk):
    task=Task.objects.get(id=pk)
    tas=Task.objects.all().filter(task_title=task)
    if request.method=='POST':
        task.delete()
        return redirect(to='index')


    return render(request,'pages/delete.html',{'task':tas})