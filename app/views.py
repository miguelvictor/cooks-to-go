from django.views.generic import TemplateView
from django.http import JsonResponse

from app.utils import normalize_recipe_params
from app.models import Recipe
from CooksToGo.serializers import RecipeSerializer

import json


class IndexView(TemplateView):
    template_name = 'app/index.html'


class WebView(TemplateView):
    template_name = 'app/webindex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        try:
            active = self.kwargs['page'].lower()
            if active == 'recipe':
                self.template_name = 'web/recipeview.html'
            elif active == 'ingredients':
                self.template_name = 'web/ingredientsView.html'
            elif active == 'virtual-basket':
                self.template_name = 'web/virtualbasket.html'
            elif active == 'settings':
                self.template_name = 'web/settings.html'
        except Exception:
            pass
        return context


def recommend_recipes(request):
    params = normalize_recipe_params(request.GET.get('q', None))
    print('Ingredients: ' + str(params))

    if params:
        params = set(params)

        exact_recipes = []
        nearly_there_recipes = []

        probable_recipes = Recipe.objects.has_ingredients(params)

        for recipe in probable_recipes:
            ingredients = set([x.ingredient.id for x in recipe.recipe_components.all()])

            if ingredients.issubset(params):
                exact_recipes.append(recipe)
            else:
                nearly_there_recipes.append({
                    'recipe': json.load(RecipeSerializer(recipe, many=False).data),
                    'missing_count': len(ingredients) - len(params)
                })

        nearly_there_recipes.sort(key=lambda x: x['missing_count'])

        return JsonResponse({
            'recipes': RecipeSerializer(exact_recipes, many=True).data,
            'nearly_there': json.dumps(nearly_there_recipes),
        })
    else:
        return JsonResponse({
            'recipes': [],
            'nearly_there': [],
        })
