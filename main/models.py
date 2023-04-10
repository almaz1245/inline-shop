from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    """категория товара"""
    title = models.CharField(max_length=255,verbose_name='категория')

    def __str__(self): # dunder method 
        return f'{self.title}'
    
class Nike(models.Model):
    """товары   батины """
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


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(unique=True, null=True, blank=True)
    def __str__(self):
        return f'{self.address}'

class OrderItem(models.Model):
    product = models.ForeignKey(to=Nike, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'
    
