from django.db import models


class MainModels(models.Model):
    title = models.CharField(max_length=20, verbose_name="Заголовок")
    name = models.CharField(max_length=100, verbose_name="Имя страницы")
    content = models.TextField(verbose_name="Контент",blank=True,null=True)

    class Meta:
        verbose_name = "Главная страница"

    def __str__(self):
        return self.name
