import json
from django.db.models import Avg
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from app.utils import normalize_recipe_params
from app.models import Recipe, Rating
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


def testing_recipe(request):
    params = set(normalize_recipe_params(request.GET.get('q', None)))

    exact_recipes = []
    nearly_there_recipes = []

    for recipe in Recipe.objects.all():
        ingredients = set([x.ingredient.id for x in recipe.recipe_components.all()])

        intersection = params & ingredients

        if len(intersection) > 0:

            difference = ingredients - intersection
            difference_length = len(difference)

            if difference_length is 0:
                exact_recipes.append(recipe)
            else:
                nearly_there_recipes.append({
                    'recipe': RecipeSerializer(recipe, many=False).data,
                    'missing': difference_length,
                })

    nearly_there_recipes.sort(key=lambda x: x['missing_count'])

    return JsonResponse({
        'recipes': RecipeSerializer(exact_recipes, many=True).data,
        'nearly_there': json.JSONDecoder().decode(json.dumps(nearly_there_recipes)),
    })


def recommend_recipes(request):
    # params = normalize_recipe_params(request.GET.get('q', None))
    # print('Ingredients: ' + str(params))

    # if params:
    #     params = set(params)

    #     exact_recipes = []
    #     nearly_there_recipes = []

    #     probable_recipes = Recipe.objects.has_ingredients(params)

    #     for recipe in probable_recipes:
    #         ingredients = set([x.ingredient.id for x in recipe.recipe_components.all()])

    #         # if ingredients.issubset(params):
    #         if ingredients == params:
    #             exact_recipes.append(recipe)
    #         else:
    #             nearly_there_recipes.append({
    #                 'recipe': RecipeSerializer(recipe, many=False).data,
    #                 'missing_count': len(ingredients) - len(params),
    #             })

    #     nearly_there_recipes.sort(key=lambda x: x['missing_count'])

    #     return JsonResponse({
    #         'recipes': RecipeSerializer(exact_recipes, many=True).data,
    #         'nearly_there': json.JSONDecoder().decode(json.dumps(nearly_there_recipes)),
    #     })

    # else:
    #     return JsonResponse({
    #         'recipes': [],
    #         'nearly_there': [],
    #     })
    params = set(normalize_recipe_params(request.GET.get('q', None)))

    exact_recipes = []
    nearly_there_recipes = []

    for recipe in Recipe.objects.all():
        ingredients = set([x.ingredient.id for x in recipe.recipe_components.all()])

        intersection = params & ingredients

        if len(intersection) > 0:

            difference = ingredients - intersection
            difference_length = len(difference)

            if difference_length is 0:
                exact_recipes.append(recipe)
            else:
                nearly_there_recipes.append({
                    'recipe': RecipeSerializer(recipe, many=False).data,
                    'missing_count': difference_length,
                })

    nearly_there_recipes.sort(key=lambda x: x['missing_count'])

    return JsonResponse({
        'recipes': RecipeSerializer(exact_recipes, many=True).data,
        'nearly_there': json.JSONDecoder().decode(json.dumps(nearly_there_recipes)),
    })

@csrf_exempt
def rating(request, id=None):
    if request.method == 'POST':
        try:
            rating = request.POST['rating']
            mac_address = request.POST['mac'].strip().upper()
            recipe = Recipe.objects.get(pk=id)
            if rating is not None and mac_address is not None:
                rate, created_status = Rating.objects.update_or_create(recipe=recipe, who=mac_address, defaults={'rating': rating})
                # rate = Rating(recipe=recipe, rating=int(rating), who=mac_address)
                # rate.save()

                #  If Rating is newly created else
                if created_status:
                    Description = 'Successfully Rated a Recipe!'
                else:
                    Description = 'Successfully Updated Your Rating!'
                # Get New Rating of Recipe
                new_rating = Rating.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
                return JsonResponse({
                    'Status': '200',
                    'Details': Description,
                    'Rating': new_rating
                })
            else:
                return JsonResponse({
                    'Status': '404',
                    'Details': 'Error! Invalid Params'
                })
        except Recipe.DoesNotExist:
            return JsonResponse({
                'Status': '404',
                'Details': 'Error!!, Recipe is not found!'
            })
        except Exception:
            return JsonResponse({
                'Status': '404',
                'Details': 'Error!!, Something Went Wrong'
            })
    else:
        return JsonResponse({
            'Status': '404',
            'Description': 'Request Not Secure!'
        })
