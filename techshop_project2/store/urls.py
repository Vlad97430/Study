from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('climate/', views.climate, name='climate'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('personal/', views.personal, name='personal'),
]