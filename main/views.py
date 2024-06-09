from django.shortcuts import render
from django.http import HttpResponse
from .models import MainModels



def index(request):
    title=MainModels.objects.get(id=1)
    return render(request,'main/index.html',{"title":title})

def about(request):
    contex = {
        "name": "О нас",
        "title": "Home - О нас", 
        "text_on_page": "Привет"

              }
    return render(request,'main/about.html',contex)
