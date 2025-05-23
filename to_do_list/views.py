from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'text': 'HOME',
        'a': ["TESTE 1", "TESTE 2", "TESTE 3", "TESTE 4", "TESTE 5", "TESTE 6", "TESTE 7", "TESTE 8", "TESTE 9"]
    }
    return render(request, 'index.html', context)
