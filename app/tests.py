from django.test import TestCase
from utils import normalize_recipe_params as qwe


class UtilsTests(TestCase):

    def test_normalize_recipe_params_should_work(self):
        quantities = [1, 2, 3]
        units = ['a', 'b', 'c']
        ingredients = ['A', 'B', 'C']

        a = qwe(quantities, units, ingredients)

        expected_result = [
            {'quantity': 1, 'unit': 'a', 'ingredient': 'A'},
            {'quantity': 2, 'unit': 'b', 'ingredient': 'B'},
            {'quantity': 3, 'unit': 'c', 'ingredient': 'C'},
        ]

        self.assertEquals(a, expected_result)

    def test_intersection(self):
        a = ['a', 'b', 'c', 'd', 'e']
        b = ['a', 'b', 'c']

        c = sorted(list(set(a) & set(b)))
        expected_result = ['a', 'b', 'c']

        self.assertEquals(c, expected_result)

        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3]

        c = sorted(list(set(a) & set(b)))
        expected_result = [1, 2, 3]

        self.assertEquals(c, expected_result)
