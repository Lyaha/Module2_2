from django.shortcuts import render
from django.urls import reverse
from .models import Recipe

def main_view(request):
    recipes = Recipe.objects.filter(created_at__year=2023)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail_view(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})