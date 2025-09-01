from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=140, unique=True, db_index=True, verbose_name='Слаг')
    description = models.TextField(blank=True, verbose_name='Опис')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    ENERGY_CLASSES = [
        ('A+++', 'A+++'),
        ('A++', 'A++'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    COLOR_CHOICES = [
        ('white', 'Білий'),
        ('black', 'Чорний'),
        ('silver', 'Сріблястий'),
        ('gray', 'Сірий'),
        ('red', 'Червоний'),
    ]

    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=220, unique=True, verbose_name='Слаг')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категорія')
    brand = models.CharField(max_length=120, verbose_name='Бренд', help_text='Виробник/бренд')
    description = models.TextField(blank=True, verbose_name='Опис', help_text='Короткий опис товару')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна', help_text='UAH')
    discount_percent = models.PositiveIntegerField(default=0, verbose_name='Знижка, %')
    stock = models.PositiveIntegerField(default=0, verbose_name='На складі')
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    warranty_months = models.PositiveIntegerField(default=12, verbose_name='Гарантія, міс', help_text='К-ть місяців гарантії')
    energy_class = models.CharField(max_length=4, choices=ENERGY_CLASSES, default='A', verbose_name='Клас енергоефективності')
    color = models.CharField(max_length=12, choices=COLOR_CHOICES, default='white', verbose_name='Колір')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.brand})"

    def final_price(self):
        if self.discount_percent:
            return self.price * (100 - self.discount_percent) / 100
        return self.price
