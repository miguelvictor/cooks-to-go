from app import models
from rest_framework import serializers, viewsets
from app.utils import normalize_recipe_params
from rest_framework import filters


class UnitOfMeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UnitOfMeasure
        fields = ('pk', 'name')


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Step
        fields = ('sequence', 'instruction')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('pk', 'banner', 'icon', 'name', 'description')


class IngredientTypeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = models.IngredientType
        fields = (
            'pk',
            'name',
            'picture',
            'ingredients',
        )


class RecipeComponentSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)
    unit_of_measure = UnitOfMeasureSerializer(many=False, read_only=True)

    class Meta:
        model = models.RecipeComponent
        fields = (
            'quantity', 'adjective', 'unit_of_measure',
            'ingredient', 'extra'
        )


class RecipeOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipe
        fields = (
            'pk',
            'url',
            'name',
            'description',
            'banner',
            'icon',
        )


class RecipeTypeSerializer(serializers.HyperlinkedModelSerializer):
    recipes = RecipeOverviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.RecipeType
        fields = (
            'pk',
            'name',
            'picture',
            'recipes',
        )


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_components = RecipeComponentSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = (
            'pk',
            'name',
            'description',
            'banner',
            'icon',
            'time_to_complete',
            'default_serving_size',
            'recipe_components',
            'steps'
        )


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')


class RecipeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer


class IngredientTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')
