from django.shortcuts import render, redirect
from to_do_list import models

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
def create_task(request):
    new_task = request.POST.get('nova_tarefa')
    task_object = models.Task(title=new_task)
    task_object.save()
    return redirect("index")


# View que cria uma nova tarefa
def delete_task(request):
    new_task = request.POST.get('nova_tarefa')
    task_object = models.Task(title=new_task)
    task_object.delete()
    return redirect("index")


# View que marca ou desmarca a tarefa como concluida
def mark_task(request):

    # Essa função usa request.POST para descobrir qual tarefa o usuario clicou.
    # No index.html as tarefas são botões cada um dentro de um formulario proprio.
    # Quando o usuario clica nessa tarefa, ele está marcando ou desmarcando
    # a tarefa ao mesmo tempo que envia o formulario com essa informação.
    # Dessa forma, o request.POST retorna somente o csrf_token e o nome do
    # botão (id da tarefa) clicado pelo usuario, então usaremos isso para
    # alterar no banco de dados, o valor "task_completed" da tarefa.

    # Pegando as tarefas
    tasks = models.Task.objects.all()

    # O nome do botão clicado pelo usuario é enviado para request.POST
    # como chave de um QueryDict, ao usar .keys() ele nos dá um Dict_keys
    # com os nomes de todas as chaves do QueryDict, o problema é que é
    # necessario percorrer esse Dict_keys para acessar seus valores.
    for key in request.POST.keys():

        # Percorrendo as tarefas para descobrir qual tarefa foi marcada
        for task in tasks:

            # Verificando se o valor do id da task corresponde com o valor do id
            if str(task.id) == str(key):  # type: ignore

                # Se o valor já está marcado, então será desmarcado
                if task.task_completed:
                    print("entrei verdadeiro")
                    task.task_completed = False
                    task.save()
                # Se o valor já está desmarcado, então será marcado
                else:
                    print("entrei falso")
                    task.task_completed = True
                    task.save()

                # Quebrando o loop pra evitar laços desnecessarios
                break

    # Adicionando variaveis a serem usandas no html
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context)


# View responsavel pela pagina da lista de tarefas
def index(request):

    if request.method == "POST":
        return mark_task(request)

    else:
        # Pegando as tarefas
        tasks = models.Task.objects.all()

        # Adicionando variaveis a serem usandas no html
        context = {
            'tasks': tasks
        }

        return render(request, 'index.html', context)
