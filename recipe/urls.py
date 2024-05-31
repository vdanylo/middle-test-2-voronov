# recipe/urls.py

from django.urls import path
from .views import main, latest_recipes, category_list

urlpatterns = [
    path('', main, name='main'),  # This line should import the 'main' view function
    path('latest-recipes/', latest_recipes, name='latest_recipes'),
    path('categories/', category_list, name='category_list'),
]
