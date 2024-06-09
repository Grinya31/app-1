from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name="index"),
    path('informations/about/',views.about,name="about"),
    path('informations/dostavka_i_oplata/',views.about,name="dostavka"),
    path('informations/contact/',views.about,name="contact"),
    
]