from django.shortcuts import render
from .models import Task
# Create your views here.
#aqui em views, vou ter que trazer todas as informaçoes da Task, para aqui passaar para o frontend
def task_list(request):
    tarefas = Task.objects.all()
    context = {
        'tarefas':tarefas
    }
    return render(request, 'tasks/task_list.html', context)

def task_ok(request):
    
    tarefas = Task.objects.filter(concluida=1)
    context = {
        'tarefas':tarefas
    }
    return render(request, 'tasks/task_list.html',context)


def task_nok(request):
    
    tarefas = Task.objects.filter(concluida=0)
    context = {
        'tarefas':tarefas
    }
    return render(request, 'tasks/task_list.html',context)

