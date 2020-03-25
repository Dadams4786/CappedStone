from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from .secrets import spoon_key

# Create your views here.

def index(request):
    return render(request, 'fudr/index.html')

def recipes(request):
    params = dict(request.GET)
    params['apiKey'] = spoon_key
    params['number'] = 3
    params['addRecipeInformation'] = True
    params['fillIngredients'] = True
    params['sort'] = 'random'
    response = requests.get('https://api.spoonacular.com/recipes/complexSearch', params=params)
    # print(response)
    spoon_recipes = json.loads(response.text)
    # print(spoon_recipes)
    spoon_recipes = spoon_recipes["results"]
    
    recipes=[]
    for spoon_recipe in spoon_recipes: 
        try:
            instructions = []
            ingredients = []
            for step in spoon_recipe["analyzedInstructions"][0]["steps"]:
                instructions.append(step["step"])
            for spoon_ingredient in spoon_recipe["missedIngredients"]:
                ingredients.append(spoon_ingredient["original"])
            ingredients = list(set(ingredients))
            ingredients.sort()
            recipes.append({
                "title" : spoon_recipe["title"],
                "image" : spoon_recipe["image"],
                "summary" : spoon_recipe["summary"],
                "instructions" : instructions,
                "ingredients" : ingredients    
            })
        except IndexError:
            continue

    return JsonResponse({"recipes" : recipes})

def randomRecipe(request):
    params = dict(request.GET)
    params['apiKey'] = spoon_key
    params['number'] = 3
    response = requests.get('https://api.spoonacular.com/recipes/random', params=params)
    random_spoon_recipes = json.loads(response.text)
    random_spoon_recipes = random_spoon_recipes["recipes"]
    recipes=[]
    for random_spoon_recipe in random_spoon_recipes:
        try: 
            instructions = []
            ingredients = []
            for step in random_spoon_recipe["analyzedInstructions"][0]["steps"]:
                instructions.append(step["step"])
            for ingredient in random_spoon_recipe["extendedIngredients"]:
                ingredients.append(ingredient["original"])
            ingredients = list(set(ingredients))
            ingredients.sort()
            recipes.append({
                "title" : random_spoon_recipe["title"],
                "image" : random_spoon_recipe["image"],
                "summary" : random_spoon_recipe["summary"],
                "instructions" : instructions,
                "ingredients" : ingredients    
            })
        except IndexError:
            continue

    return JsonResponse({"recipes" : recipes})

