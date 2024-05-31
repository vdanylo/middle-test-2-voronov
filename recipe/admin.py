# recipe/admin.py

from django.contrib import admin
from .models import Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['title', 'category__name']
    list_filter = ['created_at', 'category']
    list_display = ['title', 'created_at', 'category']
    ordering = ['title']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
