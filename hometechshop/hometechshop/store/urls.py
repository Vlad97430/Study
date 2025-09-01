from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories_view, name='categories'),
    path('products/', views.products_view, name='products'),
    path('contacts/', views.contacts, name='contacts'),
]
