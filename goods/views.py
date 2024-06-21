from django.shortcuts import render
from .models import *


def catalog(request):
    return render(request,'goods/catalog.html')

def products(request):
    return render(request,'goods/products.html')