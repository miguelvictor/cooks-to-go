from rest_framework import serializers, viewsets
from app.models import Recipe, RecipeComponent, Ingredient, Step, Rating


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('sequence', 'instruction')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('pk', 'picture', 'name', 'description')


class RecipeComponentSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = RecipeComponent
        fields = ('quantity', 'unit_of_measure', 'ingredient')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_components = RecipeComponentSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'pk',
            'name',
            'picture',
            'type',
            'recipe_components',
            'steps'
        )


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
