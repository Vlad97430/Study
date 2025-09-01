from django.shortcuts import render
from .models import Category, Product

def home(request):
    ctx = {
        'title': 'Головна • Магазин техніки для дому',
        'links': [
            {'url': 'about', 'label': 'Про магазин'},
            {'url': 'categories', 'label': 'Категорії'},
            {'url': 'products', 'label': 'Товари'},
            {'url': 'contacts', 'label': 'Контакти'},
        ],
    }
    return render(request, 'store/home.html', ctx)

def about(request):
    ctx = {'title': 'Про магазин', 'back_home': True}
    return render(request, 'store/about.html', ctx)

def categories_view(request):
    categories = Category.objects.filter(is_active=True).order_by('name')
    ctx = {'title': 'Категорії', 'categories': categories, 'back_home': True}
    return render(request, 'store/categories.html', ctx)

def products_view(request):
    products = Product.objects.filter(is_active=True).select_related('category').order_by('-created_at')
    ctx = {'title': 'Товари', 'products': products, 'back_home': True}
    return render(request, 'store/products.html', ctx)

def contacts(request):
    ctx = {'title': 'Контакти', 'back_home': True}
    return render(request, 'store/contacts.html', ctx)
