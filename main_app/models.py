from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=150)
    ingnumber = models.IntegerField()
    ingtype = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=100)
    directions = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meal.id': self.id})

