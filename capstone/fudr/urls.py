from django.urls import path
from . import views

app_name='fudr'
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes')
    patj('cards/', views.cards, name='cards')
]