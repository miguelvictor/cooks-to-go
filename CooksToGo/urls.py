from django.conf.urls import include, url
from django.contrib import admin

from app.models import Recipe
from serializers import RecipeViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^admin/', include(admin.site.urls)),
]
