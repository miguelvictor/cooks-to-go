from django.contrib import admin

from app import models


class StepInline(admin.TabularInline):
    model = models.Step
    ordering = ('sequence', 'instruction')


class RecipeAdmin(admin.ModelAdmin):
    inlines = [StepInline]
    fieldsets = [
        (None, {'fields': ['name',
                           'type', 'description', 'recipe_components']}),
        ('More Information', {'fields': ['banner', 'icon']})
    ]


class IngredientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'description']}),
        ('More Information', {'fields': ['banner', 'icon']}),
    ]

admin.site.register(models.RecipeType)
admin.site.register(models.IngredientType)
admin.site.register(models.RecipeComponent)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
