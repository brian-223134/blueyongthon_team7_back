from rest_framework import serializers
from .models import BrewingHistory

class BrewingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrewingHistory
        fields = ['id', 'user_id', 'recipe_id', 'brewed_at', 'feedback', 'bean_data']
        read_only_fields = ['id', 'user_id', 'brewed_at']