from django.db import models
from app import inflect


class RecipeManager(models.Manager):
    def has_ingredients(self, data):
        recipe_set = []

        try:
            for ingredient in data:
                to_add = []
                x = Ingredient.objects.get(pk=ingredient)
                for component in x.recipecomponent_set.all():
                    to_add.append(component.recipe)
                recipe_set.append(to_add)
        except Ingredient.DoesNotExist:
            pass

        length = len(recipe_set)

        if length > 1:
            recipe_ok = set(recipe_set[0])

            for i in range(1, length):
                try:
                    recipe_ok = recipe_ok & set(recipe_set[i])
                except IndexError:
                    pass
            return list(recipe_ok)

        # recipe_set.length here is 1 so we need to return the first element
        # which is a list containing the actual recipes
        return recipe_set[0] if length is 1 else []

    def has_ingredients_old(self, data):
        recipe_set = []

        ''' gather all recipes per ingredient '''
        for ingredient in data:
            # append each recipe list in recipe_set list
            # output : [['recipe1', 'recipe2'], ['recipe3']]
            try:
                recipe_component = RecipeComponent.objects.filter(
                    quantity__lte=ingredient['quantity'],
                    unit_of_measure__pk=ingredient['unit'],
                    ingredient__pk=ingredient['ingredient'],
                )
                recipes = recipe_component[0].recipe_set.all()
                recipe_set.append(recipes)
            except IndexError:
                pass

        ''' save recipe_set.length for reusability '''
        length = len(recipe_set)

        if length > 1:
            recipe_ok = set(recipe_set[0])

            for i in range(1, length):
                try:
                    recipe_ok = recipe_ok & set(recipe_set[i])
                except IndexError:
                    pass

            return recipe_ok

        # recipe_set.length here is 1 so we need to return the first element
        # which is a list containing the actual recipes
        return recipe_set[0] if length is 1 else []


class RecipeType(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()

    def __unicode__(self):
        return self.name.capitalize()


class IngredientType(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()

    def __unicode__(self):
        return self.name.capitalize()


class Ingredient(models.Model):
    banner = models.URLField()
    description = models.TextField()
    icon = models.URLField()
    name = models.CharField(max_length=255)
    type = models.ForeignKey(IngredientType, related_name='ingredients')

    def __unicode__(self):
        return self.name.capitalize()


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.URLField()
    banner = models.URLField()
    default_serving_size = models.IntegerField()
    time_to_complete = models.FloatField()
    categories = models.ManyToManyField(RecipeType, related_name='recipes')

    objects = RecipeManager()

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name.capitalize()


class RecipeComponent(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_components')
    quantity = models.FloatField()
    adjective = models.CharField(max_length=255, blank=True)
    unit_of_measure = models.ForeignKey(UnitOfMeasure)
    ingredient = models.ForeignKey(Ingredient)
    extra = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        p = inflect.engine()

        if (self.quantity).is_integer():
            string = "%s " % str(int(self.quantity))
        else:
            string = "%s " % str(self.quantity)

        if self.unit_of_measure.name != 'generic':
            string += "%s of " % p.plural(self.unit_of_measure.name, int(self.quantity))

        if self.adjective:
            string += "%s " % self.adjective

        string += self.ingredient.name.lower()

        return string


class Step(models.Model):
    sequence = models.IntegerField(default=1)
    instruction = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='steps')

    def __unicode__(self):
        # return 'Step ' + str(self.sequence) + ' of ' + self.recipe.name
        return 'Step %s' % str(self.sequence)

    class Meta:
        ordering = ['sequence']


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    recipe = models.ForeignKey(Recipe, related_name='ratings')
    who = models.CharField(max_length='20')

    def __unicode__(self):
        return self.rating
