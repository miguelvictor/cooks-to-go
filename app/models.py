from django.db import models


class RecipeManager(models.Manager):
    def has_ingredients(self, ingredients):
        q = set([int(x) for x in ingredients.strip().split(',')])
        recipes = self.all()
        recipes_we_wanted = []

        for k in recipes:
            pks = set([x.ingredient.pk for x in k.recipe_components.all()])
            if q < pks or q == pks:
                recipes_we_wanted.append(k)

        return recipes_we_wanted


class RecipeType(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()
    type = models.ForeignKey(RecipeType, related_name='recipes')

    objects = RecipeManager()

    def __unicode__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    sequence = models.IntegerField(default=1)
    instruction = models.TextField()

    def __unicode__(self):
        return 'Step ' + str(self.sequence) + ' of ' + self.recipe.name


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ratings')
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rating


class IngredientType(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    picture = models.URLField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.ForeignKey(IngredientType, related_name='ingredients')

    def __unicode__(self):
        return self.name


class RecipeComponent(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_components')
    quantity = models.IntegerField(default=1)
    unit_of_measure = models.CharField(max_length=255)  # to 'unit_of_measure'
    ingredient = models.OneToOneField(Ingredient)  # rename to 'ingredient'

    def __unicode__(self):
        return str(self.quantity) + ' ' \
            + self.unit_of_measure + ' of ' \
            + self.ingredient.name
