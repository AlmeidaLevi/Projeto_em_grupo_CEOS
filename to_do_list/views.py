from django.shortcuts import render, redirect
from to_do_list import models
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.


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


# View que cria uma nova tarefa
def create_task(request, username):

    new_task = request.POST.get('nova_tarefa')
    task_object = models.Task(title=new_task)
    try:
        user = User.objects.get(username=username)
        task_object.owner = user
        task_object.save()
    except User.DoesNotExist:
        task_object.save()

    return redirect("index")


# View que marca ou desmarca a tarefa como concluida
def mark_task(request, task_id):
    task_object = models.Task.objects.get(id=task_id)
    if task_object.task_completed:
        task_object.task_completed = False
        task_object.save()
    else:
        task_object.task_completed = True
        task_object.save()

    return redirect("index")


# View que deleta uma tarefa
def delete_task(request, task_id):
    task_object = models.Task.objects.get(id=task_id)
    task_object.delete()
    return redirect("index")


# View que atualiza uma tarefa
def update_task(request, task_id):
    new_title = request.POST.get("novo_titulo")
    task_object = models.Task.objects.get(id=task_id)
    task_object.title = new_title
    task_object.save()
    return redirect("index")


# View responsavel pela pagina da lista de tarefas
def index(request):

    # Pegando as tarefas
    tasks = models.Task.objects.all()

    # Adicionando variaveis a serem usandas no html
    context = {
        'tasks': tasks,
    }

    return render(request, 'index.html', context)


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
        user = User.objects.get(username=username)
        if user.password == password:
            auth.login(request, user)
            messages.info(request, "usuario logado com sucesso")
        else:
            messages.error(request, "Senha incorreta")
    except User.DoesNotExist:
        messages.error(request, "Usuário não existe")

    return redirect("index")


def logout_view(request):
    auth.logout(request)
    messages.info(request, "deslogado")
    return redirect("index")


def sign_up_view(request):
    username = request.POST.get('sign_up_user')
    password = request.POST.get('sign_up_password')
    try:
        user = User.objects.get(username=username)
        messages.error(request, f"usuario {user} já existe")
    except User.DoesNotExist:
        new_user = User(username=username, password=password)
        new_user.save()
        auth.login(request, new_user)
        messages.info(request, "Usuario criado com SUCESSO")

    return redirect("index")
