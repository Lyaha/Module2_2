from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from .models import Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_recipe_detail_view1(self):
       category = Category.objects.create(name='Test Category')
       recipe = Recipe.objects.create(title='Test Recipe', description='Recipe content', ingredients = "Recipe ingridient", instructions = 'Recipe instructions', category=category)
       response = self.client.get(reverse('recipe_detail', kwargs={'pk': recipe.id}))
       self.assertEqual(response.status_code, 200)
       self.assertContains(response, 'Test Recipe')
       self.assertContains(response, 'Recipe content')
    

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)