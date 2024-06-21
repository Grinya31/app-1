from django.shortcuts import render
from django.http import HttpResponse

from goods.models import *

def index(request):
    category=Categories.objects.all()
    context={'category':category}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact():
    return HttpResponse("Контакт")

def dostavka():
    return HttpResponse('Доставка')