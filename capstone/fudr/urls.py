from django.urls import path
from . import views

app_name='fudr'
urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('randomrecipe/', views.randomRecipe, name='randomRecipe'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout/', views.logout, name='logout'),
    
    
    
]