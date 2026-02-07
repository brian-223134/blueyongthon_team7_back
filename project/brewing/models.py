from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class BrewingHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    brewed_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60, default="")
    feedback = models.TextField(blank=True, null=False)
    bean_data = models.JSONField(blank=True, null=False)
    # bean_data 예시 : { "country": "에티오피아", "estate": "농장 이름", "variety": "품종", "process": "가공 방식" }
