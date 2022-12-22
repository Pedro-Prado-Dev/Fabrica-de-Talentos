from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def homepage(request):
    if request.method == "GET":
        nome = 'Pedro'
        return render(request, 'homepage.html', {'Home do':nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        usuario = Usuario(nome=nome, idade=idade) 
        usuario.save()

        #usuarios = Usuario.objects.all()
        #print(usuarios)      ->chama os usuarios do banco de dados 
        
        return HttpResponse('Cadastro concluido')

def login(request):
    return HttpResponse('Faça seu Login')

# Create your views here.
