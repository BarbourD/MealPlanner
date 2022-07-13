from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CHOWTIME = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('S', 'Snack')
)

# Create your models here.

class List(models.Model):
    quantity = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.quantity} {self.item}"
    def get_absolute_url(self):
        return reverse('lists_detail', kwargs={'pk': self.id})

class Meal(models.Model):
    day = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    lists = models.ManyToManyField(List)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meal_id': self.id})

class Recipe(models.Model):
    ingredients = models.CharField(max_length=100)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE) 
    def __str__(self):
        return f"Recipe Ingredients {self.ingredients}"
    
class Directions(models.Model):  
    directions = models.TextField(max_length=1000)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    def __str__(self):
        return f"Recipe Directions {self.directions}"
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for meal_id: {self.meal_id} @{self.url}"