from django.views.generic import TemplateView
from django.http import JsonResponse

from app.utils import normalize_recipe_params
from app.models import Recipe
from CooksToGo.serializers import RecipeSerializer


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

    if params:
        recipes = []

        recipes_nearly_there = Recipe.objects.has_ingredients(params)

        for recipe in Recipe.objects.all():
            ingredients = [x.ingredient.id for x in recipe.recipe_components.all()]
            if ingredients == params:
                recipes.append(recipe)

        recipes_nearly_there = list(set(recipes_nearly_there) - set(recipes))

        return JsonResponse({
            'recipes': RecipeSerializer(recipes, many=True).data,
            'nearly_there': RecipeSerializer(recipes_nearly_there, many=True).data,
        })
    else:
        return JsonResponse({
            'recipes': [],
            'nearly_there': [],
        })
