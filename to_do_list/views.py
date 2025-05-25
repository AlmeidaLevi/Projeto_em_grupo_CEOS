from django.shortcuts import render, redirect
from to_do_list import models

# Create your views here.

# View responsavel por exibir a lista de tarefas
def index(request):
    # Pegando as tarefas
    tasks = models.Task.objects.all().order_by("task_completed")

    # Adicionando variaveis a serem usandas no html
    context = {
        'text': 'HOME',
        'tasks': tasks
    }

    return render(request, 'index.html', context)


# View responsavel pelas pesquisas
def search(request):
    search_value = request.GET.get('q', '')

    if search_value.isspace() or search_value == '':
        return redirect("index")

    tasks = models.Task.objects.all()\
        .filter(title__icontains=search_value)\
        .order_by("task_completed")


    context = {
        'text': search_value,
        'tasks': tasks
    }
    return render(request, 'index.html', context)
