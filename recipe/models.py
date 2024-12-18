from django.db import models

# Create your models her
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="recipe/recipe_img")

