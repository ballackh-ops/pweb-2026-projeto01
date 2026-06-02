from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def index(request):
    dados_usuario = {"nome": "Michael Douglas", "idade": 23}
    return render(request, "index.html", dados_usuario)