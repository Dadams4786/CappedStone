from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from .secrets import spoon_key

# Create your views here.

def index(request):
    return render(request, 'fudr/index.html')

def recipes(request):
    # text = request.GET['text']
    # print(text)
    params = dict(request.GET)
    params['apiKey'] = spoon_key
    params['number'] = 2
    params['addRecipeInformation'] = True
    response = requests.get('https://api.spoonacular.com/recipes/complexSearch', params=params)
    recipes = json.loads(response.text)
    return JsonResponse(recipes)

def cards(request):
    params = dict(request.GET)
    params['apiKey'] = spoon_key
    response = request.get('https://api.spoonacular.com/recipes/visualizeRecipe', params=params)
    recipe_cards = json.loads(response)
    return JsonResponse(recipe_cards)