
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='Опис відсутній')

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Техніка'),
        ('appl', 'Побутова техніка'),
        ('mob', 'Смартфони'),
        ('comp', 'Комп’ютери'),
    ]

    name = models.CharField(max_length=200, verbose_name='Назва товару')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0, verbose_name='Кількість на складі')
    description = models.TextField(blank=True, default='Опис не надано')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    product_type = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='tech',
        verbose_name='Тип товару'
    )

    def __str__(self):
        return self.name
