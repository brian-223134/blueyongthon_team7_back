from django.urls import path

from .views import BrewingHistoryView, BrewingHistoryDetailView

urlpatterns = [
	path('brewing-history/', BrewingHistoryView.as_view(), name='brewing-history-list-create'),
	path('brewing-history/<int:history_id>/', BrewingHistoryDetailView.as_view(), name='brewing-history-detail'),
]