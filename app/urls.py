from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recipes/all$', views.RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipes/get$', views.RecipeView.as_view(), name='recipe'),
]
