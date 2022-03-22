from django.db import models
from menus.models import Day, Menu



class RecipeTypeManager(models.Manager):
    def recipe_type_validator(self, postData):
        errors = {}
        if len(postData['recipe_type']) < 2:
            errors['recipe_type'] = 'Recipe Type must include 2 or more characters'
        
        return errors

class RecipeType(models.Model):
    type_name = models.CharField(max_length=45)
    objects = RecipeTypeManager()





class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        errors = {}
        recipes = Recipe.objects.all()
        if len(postData['title']) < 1:
            errors['title'] = 'Recipe title is required'
        
        return errors

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    days = models.ManyToManyField(Day, related_name = 'recipes')
    recipe_types = models.ManyToManyField(RecipeType, related_name = 'recipes')
    menus = models.ManyToManyField(Menu, related_name='recipes')
    objects = RecipeManager()





class PhotoManager(models.Manager):
    def photo_validator(self, postData):
        errors = {}
        if not['photo_upload']:
            errors['photo'] = "Image is required for photo upload"
        
        return errors

class Photo(models.Model):
    photo_upload = models.ImageField
    recipe = models.ForeignKey('Recipe', blank=True, null=True, on_delete = models.CASCADE)
    objects = PhotoManager()

class MealTypeManager(models.Manager):
    def meal_type_validator(self, postData):
        errors = {}
        if len(postData['meal_type']) < 2:
            errors['meal_type'] = 'Meal Type must include 2 or more characters'
        
        return errors
        

class MealType(models.Model):
    meal_name = models.CharField(max_length=45)
    recipes= models.ManyToManyField(Recipe, related_name='meals')
    # days= models.ManyToManyField(Day, related_name='meals')
    objects = MealTypeManager()

