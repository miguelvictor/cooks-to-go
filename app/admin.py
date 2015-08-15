from django.contrib import admin

from app import models


class StepInline(admin.TabularInline):
    model = models.Step


class RecipeInline(admin.TabularInline):
    model = models.RecipeComponent


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            'name', 'type', 'description',
            'default_serving_size', 'time_to_complete',
        ]}),
        ('More Information', {'fields': ['banner', 'icon']}),
    ]

    inlines = (RecipeInline, StepInline)
    search_fields = 'name', 'description'
    list_filter = 'type',


class IngredientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'type', 'description']}),
        ('More Information', {'fields': ['banner', 'icon']}),
    ]

    search_fields = 'name', 'description'
    list_filter = 'type',

admin.site.register(models.RecipeType)
admin.site.register(models.IngredientType)
admin.site.register(models.RecipeComponent)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
