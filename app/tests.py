from django.test import TestCase

from utils import normalize_recipe_params as qwe
from models import Recipe

'''
class UtilsTests(TestCase):

    def test_normalize_recipe_params_should_work(self):
        quantities = '1,2,3'
        units = '4,5,6'
        ingredients = '7,8,9'

        a = qwe(quantities, units, ingredients)

        expected_result = [
            {'quantity': 1, 'unit': 4, 'ingredient': 7},
            {'quantity': 2, 'unit': 5, 'ingredient': 8},
            {'quantity': 3, 'unit': 6, 'ingredient': 9},
        ]

        self.assertEquals(a, expected_result)


class CustomRecipeManagerTests(TestCase):

    fixtures = ['test_data.json']

    def test_recipe_has_ingredients_with_existing_recipe(self):
        quantities = '0.5,2,2,1,0.25,0.25'
        units = '5,1,1,1,2,2'
        ingredients = '2,3,4,5,6,7'

        data = qwe(quantities, units, ingredients)

        recipes = Recipe.objects.has_ingredients(data)

        self.assertEquals(len(recipes), 1)

    def test_recipe_has_ingredients_with_incorrect_params(self):
        quantities = '1,2,3,4'
        units = '5,2,1,4'
        ingredients = '7,2,1,4'

        data = qwe(quantities, units, ingredients)

        recipes = Recipe.objects.has_ingredients(data)

        self.assertFalse(recipes)
'''


class FindRecipesTests(TestCase):

    fixtures = ['test_data']

    def test_naa_sya_tanan_ingredients(self):
        ingredients = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        recipes = Recipe.objects.has_ingredients(ingredients)
        self.assertEquals(len(recipes), 1)

    def test_naa_sya_subset_sa_ingredients(self):
        ingredients = [1, 2, 3]
        recipes = Recipe.objects.has_ingredients(ingredients)
        self.assertEquals(len(recipes), 1)

    def test_wala_syay_ingredients(self):
        ingredients = [11, 12, 123]
        recipes = Recipe.objects.has_ingredients(ingredients)
        self.assertEquals(len(recipes), 0)
