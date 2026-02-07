from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.RecipeView.as_view(), name='recipe-list'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('<int:recipe_pk>/steps/', views.RecipeStepView.as_view(), name='recipe-steps'),
    path('<int:recipe_pk>/steps/<int:step_pk>/', views.RecipeStepDetailView.as_view(), name='recipe-step-list'),
]
