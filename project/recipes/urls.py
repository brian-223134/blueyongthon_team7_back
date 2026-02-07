from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'recipe-steps', views.RecipeStepsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]