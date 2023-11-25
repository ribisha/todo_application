from django.shortcuts import render, redirect
from .models import todo
from .forms import TaskForm


def index(request):
    task_view=todo.objects.all()
    if request.method=="POST":
        task_name=request.POST.get('task_name', '')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=todo(task_name=task_name, priority=priority, date=date)
        task.save()
    return render(request,'index.html',{'task_view':task_view})

def delete(request,id):
    task=todo.objects.get(id=id)
    task.delete()
    return redirect('/')

def update(request,task_id):
    task=todo.objects.get(id=task_id)
    f=TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})



