from django.contrib import admin
from .models import MainModels

@admin.register(MainModels)

class MainModelsAdmin(admin.ModelAdmin):
    list_display=["title","name","content"]
