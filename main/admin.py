from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    fields=['name','slug']
    prepopulated_fields={'slug':('name',)}


# Register your models here.
