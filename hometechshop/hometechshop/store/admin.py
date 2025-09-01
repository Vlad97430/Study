from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'discount_percent', 'stock', 'is_active')
    list_editable = ('price', 'discount_percent', 'stock', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'brand', 'is_active', 'energy_class', 'color')
    search_fields = ('name', 'brand', 'description')
