from django.contrib import admin
from .models import Categories,Goodsmodels

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    fields=['name','slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Goodsmodels)
class GoodsAdmin(admin.ModelAdmin):
    list_display=['name','slug',]
    fields=['name','slug']
    prepopulated_fields={'slug':('name',)}

