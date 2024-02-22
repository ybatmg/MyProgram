from django.shortcuts import render,redirect
from . models import Task
from home.task_form import Taskform

# Create your views here.
def index(request):
    tasklist = Task.objects.all()

    return render(request,'index.html',{'form':tasklist})

def tasks(request):
    if request.method == "POST":
        task_form=Taskform(request.POST)
        if task_form.is_valid():
            print(task_form)
            task_form.save()
            return redirect('index')
        
    task_form=Taskform()
    return render(request,'create_task.html',{'form':task_form})

def deletetask(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('index')

def updatetask(request,id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task_form = Taskform(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    task_form=Taskform(instance=task)
    return render(request,'create_task.html',{'form':task_form})