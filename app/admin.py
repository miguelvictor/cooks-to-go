from django.contrib import admin

from app import models


class IngredientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('More Information', {'fields': ['picture']}),
    ]


class RecipeComponentInline(admin.TabularInline):
    model = models.RecipeComponent


class StepInline(admin.TabularInline):
    model = models.Step


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        RecipeComponentInline,
        StepInline,
    )

admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)