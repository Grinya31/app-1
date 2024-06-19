from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=30,verbose_name='Имя категории')
    slug=models.SlugField(max_length=20,unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        def __str__(self):
            return f"{self.name}"
# Create your models here.
