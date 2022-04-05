from django.shortcuts import redirect, render
from .form import *
from .models import Task
# Create your views here.

def index(request):
    task=Task.objects.all()
    return render(request,'pages/index.html',{'task':task})
def users(request):
    if request.method=='POST':
        task_title=TitleForm(request.POST)
        task=ContentForm(request.POST)
        category=CategoryForm(request.POST)
        status=StatusForm(request.POST)
        begin=BeginForm(request.POST)
        end=EndForm(request.POST)
        if task_title.is_valid() and task.is_valid()\
             and begin.is_valid() and end.is_valid()\
             and category.is_valid() and category.is_valid():
            task_title=request.POST.get('title')
            # task=request.POST.get('task')
            # category_post=request.POST.get('category')
            # status_post=request.POST.get('status')
            # begin=category.cleaned_data.get('begin')
            # end=category.cleaned_data.get('end')
            data=Task(
                task_title=task_title,
                task=task.cleaned_data.get('task'),
                status=request.POST.get('status'),
                category=request.POST.get('category'),
                begin=begin.cleaned_data.get('begin'),
                end=end.cleaned_data.get('end')
            )
            data.save()
            return redirect(to='index')
    # Forms
    title=TitleForm()
    content=ContentForm()
    time_begin=BeginForm()
    time_end=EndForm()
    category=CategoryForm()
    status=StatusForm()
    context={
        'title':title,
        'content':content,
        'category':category,
        'status':status,
        'begin':time_begin,
        'end':time_end,
    }
    return render(request,'pages/users.html',context)
def register(request):
    return render(request,'pages/register.html')
