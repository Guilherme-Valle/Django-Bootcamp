from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello world</h1>')
    pass


def cadastro(request):
    return HttpResponse('<h1>Cadastro</h1>')
    pass


def lista(request):
    return HttpResponse('<h1>Lista</h1>')
    pass



