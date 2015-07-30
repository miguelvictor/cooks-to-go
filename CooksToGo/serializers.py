from app import models
from rest_framework import serializers, viewsets


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Step
        fields = ('sequence', 'instruction')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('pk', 'picture', 'name', 'description')


class RecipeComponentSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = models.RecipeComponent
        fields = ('quantity', 'unit_of_measure', 'ingredient')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_components = RecipeComponentSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = (
            'pk',
            'name',
            'picture',
            'type',
            'recipe_components',
            'steps'
        )


class RecipeTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.RecipeType
        fields = (
            'pk',
            'name',
            'picture',
            'recipes',
        )


class IngredientTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.IngredientType
        fields = (
            'pk',
            'name',
            'picture',
            'ingredients',
        )


class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        ingredients = request.GET.get('ingredients', None)
        if ingredients is not None:
            self.queryset = models.Recipe.objects.has_ingredients(ingredients)
        return super(RecipeViewSet, self).list(self, request)


class RecipeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RecipeType.objects.all()
    serializer_class = RecipeTypeSerializer


class IngredientTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer
