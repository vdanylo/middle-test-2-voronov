# recipe/views.py

from django.shortcuts import render
from .models import Recipe, Category

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'main.html', {'latest_recipes': latest_recipes})
def latest_recipes(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'latest_recipes.html', {'latest_recipes': latest_recipes})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
