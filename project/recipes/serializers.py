from rest_framework import serializers
from .models import Recipe, RecipeSteps



class RecipeStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSteps
        fields = ['id', 'recipe_id', 'time', 'amount', 'guide']
        read_only_fields = ['recipe_id']


class RecipeSerializer(serializers.ModelSerializer):
    steps = RecipeStepsSerializer(many=True, source='recipesteps_set')

    class Meta:
        model = Recipe
        fields = ['id', 'user_id', 'name', 'description', 'temperature','bean_weight', 'grind_size', 'is_shared', 'steps']
        read_only_fields = ['user_id']

    def create(self, validated_data):
        steps_data = validated_data.pop('recipesteps_set')
        recipe = Recipe.objects.create(**validated_data)
        for step_data in steps_data:
            RecipeSteps.objects.create(recipe_id=recipe, **step_data)
        return recipe

    def update(self, instance, validated_data):
        steps_data = validated_data.pop('recipesteps_set', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if steps_data is not None:
            instance.recipesteps_set.all().delete()
            for step_data in steps_data:
                RecipeSteps.objects.create(recipe_id=instance, **step_data)

        return instance




