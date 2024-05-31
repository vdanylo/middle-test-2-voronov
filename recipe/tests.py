from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(title='Test Recipe', description='Test description', category=self.category)

    def test_main_view(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_latest_recipes_view(self):
        url = reverse('latest_recipes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'latest_recipes.html')

    def test_category_list_view(self):
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')


class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(title='Test Recipe', description='Test description', category=self.category)
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.description, 'Test description')
        self.assertEqual(recipe.category, self.category)

class CategoryModelTestCase(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')