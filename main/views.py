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

def task_create(request):

    if request.method == 'POST': #vERIFICAÇAO SE È UM METODO POST

        titulo = request.POST.get('titulo', "").strip()
        descricao = request.POST.get('descricao', "").strip()
        concluida = request.POST.get('concluida', "").strip()
        prioridade = request.POST.get('prioridade', "").strip()
        data_limite = request.POST.get('data_limite', "").strip()

        context = {
            'opcoes_prioridade': Task.Priority.choices,
        }
        return render(request, 'task/task_form.html', context)