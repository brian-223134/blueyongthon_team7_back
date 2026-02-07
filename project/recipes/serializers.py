from rest_framework import serializers
from .models import Recipe, RecipeSteps

class RecipeStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSteps
        fields = ['__all__']


class RecipeSerializer(serializers.ModelSerializer):
    steps = RecipeStepsSerializer(many=True, read_only=True, source='recipesteps_set')
    
    class Meta:
        model = Recipe
        fields = ['__all__']