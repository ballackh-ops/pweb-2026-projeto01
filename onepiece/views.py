from django.shortcuts import render

def index(request):
    return render(request, "onepiece/index.html")

def sobre(request):
    
    return render(request, "onepiece/sobre.html")

def elenco(request):

    lista_usuarios = [
            {"nome": "Iñaki Godoy", "idade": 19, "cidade": "Cidade do México"},
            {"nome": "Emily Rudd", "idade": 19, "cidade": "Spring Valley"},
            {"nome": "Jacob Gibson", "idade": 19, "cidade": "Denver"},
            {"nome": "Taz Skylar", "idade": 19, "cidade": "Tenerife"},
            {"nome": "Mackenyu", "idade": 19, "cidade": "Little Tokyo"},
        ]
    
    context = {"usuarios": lista_usuarios,}
    return render(request, "onepiece/elenco.html", context)
