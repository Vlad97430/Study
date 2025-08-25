from django.shortcuts import render

def home(request):
    context = {'title': 'Головна - Магазин техніки для дому'}
    return render(request, 'store/home.html', context)

def kitchen(request):
    context = {'title': 'Кухонна техніка'}
    return render(request, 'store/section.html', context)

def cleaning(request):
    context = {'title': 'Техніка для прибирання'}
    return render(request, 'store/section.html', context)

def climate(request):
    context = {'title': 'Кліматична техніка'}
    return render(request, 'store/section.html', context)

def entertainment(request):
    context = {'title': 'Техніка для розваг'}
    return render(request, 'store/section.html', context)

def personal(request):
    context = {'title': 'Персональна техніка'}
    return render(request, 'store/section.html', context)