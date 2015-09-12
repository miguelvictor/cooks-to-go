from django.conf.urls import include, url
from django.contrib import admin

from . import serializers

from app.views import recommend_recipes

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'recipes', serializers.RecipeViewSet)
router.register(r'recipe-types', serializers.RecipeTypeViewSet)
router.register(r'ingredients', serializers.IngredientViewSet)
router.register(r'ingredient-types', serializers.IngredientTypeViewSet)

urlpatterns = [
    url(r'^', include('app.urls', namespace='app')),
    url(r'^api/', include(router.urls)),
    url(r'^api/recipes/recommend$', recommend_recipes),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^admin/', include(admin.site.urls)),
]
