from django.views import generic
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from models import Recipe


class RecipeListView(generic.View):

    ''' kini nga class kay igo ra mureturn sa list sa tanang recipes '''

    def get(self, request):
        recipes = Recipe.objects.all()
        return JsonResponse(
            serializers.serialize("json", recipes),
            safe=False
        )


class RecipeView(generic.View):

    ''' kini nga class kay mureturn sa full details sa usa ka recipe '''

    def get(self, request):
        recipe = get_object_or_404(Recipe, pk=request.GET.get('recipe'))
        return JsonResponse(
            serializers.serialize(
                "json",
                [recipe],
                fields=('name', 'picture', 'type', )
            ),
            safe=False
        )
