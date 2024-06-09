from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    contex = {
        "name": "Магазин мебели Home",
        "title": "Главная"
              }
    return render(request,'main/index.html',contex)

def about(request):
    contex = {
        "name": "О нас",
        "title": "Home - О нас", 
        "text_on_page": "Привет"

              }
    return render(request,'main/about.html',contex)
