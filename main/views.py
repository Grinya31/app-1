from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse('Домашняя страница')

def about(request):
    return HttpResponse('О нас')