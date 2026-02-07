from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.IntegerField(default=0, null=False)
    grind_size = models.IntegerField(default=0, null=False)
    bean_weight = models.IntegerField(default=0, null=False)
    is_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class RecipeSteps(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    time = models.IntegerField()
    amount = models.IntegerField()
    guide = models.CharField(max_length=64)

    def __str__(self):
        return f"Step {self.step_number} for {self.recipe_id.name}"
    
