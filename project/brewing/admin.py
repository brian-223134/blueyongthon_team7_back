from django.contrib import admin
from .models import BrewingHistory

@admin.register(BrewingHistory)
class BrewingHistoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'user_id', 'recipe_id', 'brewed_at')
	list_filter = ('brewed_at',)
	search_fields = ('user_id__username', 'recipe_id__name')

