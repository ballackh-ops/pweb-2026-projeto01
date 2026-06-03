from django.shortcuts import render

def index(request):
    return render(request, "onepiece/index.html")

def usuarios(request):
    
    lista_usuario = [
            {"Nome": "Iñaki Godoy", "Idade": 19, "Cidade": "Cidade do México"},
            {"Nome": "Emily Rudd", "Idade": 19, "Cidade": "Spring Valley"},
            {"Nome": "Jacob Gibson", "Idade": 19, "Cidade": "Denver"},
            {"Nome": "Taz Skylar", "Idade": 19, "Cidade": "Tenerife"},
            {"Nome": "Mackenyu", "Idade": 19, "Cidade": "Little Tokyo"},
        ]
    
    context = {"usuarios": lista_usuario,}
    return render(request, "onepiece/index.html", context)
