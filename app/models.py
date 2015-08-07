from django.db import models


class RecipeManager(models.Manager):
    def has_ingredients(self, data):
        recipe_set = []

        ''' gather all recipes per ingredient '''
        for ingredient in data:
            # append each recipe list in recipe_set list
            # output : [['recipe1', 'recipe2'], ['recipe3']]
            try:
                recipe_component = RecipeComponent.objects.filter(
                    quantity__gte=ingredient['quantity'],
                    unit_of_measure__name__iexact=ingredient['unit'],
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
                    recipe_ok = list(recipe_ok & set(recipe_set[i]))
                except IndexError:
                    pass

            return recipe_ok

        # recipe_set.length here is 1 so we need to return the first element
        # which is a list containing the actual recipes
        return recipe_set[0]


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
    description = models.CharField(max_length=255)
    icon = models.URLField()
    name = models.CharField(max_length=255)
    type = models.ForeignKey(IngredientType, related_name='ingredients')

    def __unicode__(self):
        return self.name.capitalize()


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class RecipeComponent(models.Model):
    ingredient = models.OneToOneField(Ingredient)
    quantity = models.FloatField()
    unit_of_measure = models.ForeignKey(UnitOfMeasure)
    extra = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        if not self.extra:
            return "%s %s of %s" % (
                str(self.quantity),
                self.unit_of_measure.name,
                self.ingredient.name
            )
        else:
            return "%s %s of %s, %s" % (
                str(self.quantity),
                self.unit_of_measure.name,
                self.ingredient.name,
                self.extra
            )


class Recipe(models.Model):
    banner = models.URLField()
    icon = models.URLField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    recipe_components = models.ManyToManyField(RecipeComponent)
    type = models.ForeignKey(RecipeType, related_name='recipes')

    objects = RecipeManager()

    def __unicode__(self):
        return self.name.capitalize()


class Step(models.Model):
    sequence = models.IntegerField(default=1)
    instruction = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='steps')

    def __unicode__(self):
        return 'Step ' + str(self.sequence) + ' of ' + self.recipe.name


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    recipe = models.ForeignKey(Recipe, related_name='ratings')
    who = models.CharField(max_length='20')

    def __unicode__(self):
        return self.rating
