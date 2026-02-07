from django.contrib import admin
from .models import Recipe, RecipeSteps

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeSteps)