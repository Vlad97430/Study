from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'Головна сторінка'})

def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})

def categories(request):
    return render(request, 'categories.html', {'title': 'Категорії'})

def products(request):
    return render(request, 'products.html', {'title': 'Товари'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакти'})
