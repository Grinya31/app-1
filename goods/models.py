from django.db import models



class Categories(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True)

    class Meta:
        db_table="Category"
        verbose_name="Категория"
        verbose_name_plural="Категории"
   
    def __str__(self):
        return f"{self.name}"



class Goodsmodels(models.Model):
    name=models.CharField(max_length=200,verbose_name='Название товара')
    slug=models.SlugField(verbose_name='слаг',unique=True)
    description=models.TextField(verbose_name='Описание товара',blank=True,null=True)
    price=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Стоимость')
    image=models.ImageField(upload_to='goods_images')
    discount=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='Скидка')
    quantity=models.PositiveIntegerField(default=0,verbose_name='Количество')
    category=models.ForeignKey(Categories,on_delete=models.PROTECT)
    
    
    class Meta:
        db_table="Goods"
        verbose_name="Продукт"
        verbose_name_plural="Продукты"
    

    
    def __str__(self):
        return f"{self.name}"
