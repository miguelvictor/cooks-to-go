from django.contrib import admin

from app import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe


class IngredientInline(admin.StackedInline):
    model = models.Ingredient


class RecipeComponentInline(admin.TabularInline):
    model = models.RecipeComponent


class StepInline(admin.TabularInline):
    model = models.Step


class RecipeTypeAdmin(admin.ModelAdmin):
    inlines = (
        RecipeInline,
    )


class RecipeAdmin(admin.ModelAdmin):
    inlines = (
        RecipeComponentInline,
        StepInline,
    )


class IngredientTypeAdmin(admin.ModelAdmin):
    inlines = (
        IngredientInline,
    )


class IngredientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'description']}),
        ('More Information', {'fields': ['picture']}),
    ]

admin.site.register(models.RecipeType, RecipeTypeAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.IngredientType, IngredientTypeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
