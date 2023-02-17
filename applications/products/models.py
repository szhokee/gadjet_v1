from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
   
    title = models.CharField('Название продукта', max_length=50, null=True, blank=True)
    model = models.CharField('Модель', max_length=50, null=True)
    price = models.DecimalField('сом', max_digits=1000, decimal_places=10)
    color = models.CharField(max_length=50, null=True)
    nalich = models.BooleanField(verbose_name='В наличии')
    description = models.TextField('Описание продукта', max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f'{self.product.title}'     


    

