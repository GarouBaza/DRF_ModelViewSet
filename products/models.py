from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Катеории', related_name='products')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'