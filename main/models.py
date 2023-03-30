from django.db import models

# Create your models here.
class Category(models.Model):
    """категория товара"""
    title = models.CharField(max_length=255,verbose_name='категория')

    def __str__(self): # dunder method 
        return f'{self.title}'
    
class Nike(models.Model):
    """"""
    title = models.CharField(max_length=255, verbose_name='название товара')
    description = models.TextField(verbose_name='описания')
     
    images = models.ImageField(upload_to='products')
    price = models.PositiveIntegerField(verbose_name="цена")
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE, verbose_name='категория ')


    def __str__(self) -> str:
        return f'{self.title}'

class Image(models.Model):
    sneakers = models.ForeignKey(to=Nike, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sneakers_images', verbose_name='изображение')
