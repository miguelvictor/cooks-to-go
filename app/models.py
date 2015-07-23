from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    sequence = models.IntegerField(default=0)
    instruction = models.TextField()

    def __unicode__(self):
        return 'Step ' + str(self.sequence) + ' of ' + self.recipe.name


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ratings')
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rating


class Ingredient(models.Model):
    picture = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

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
