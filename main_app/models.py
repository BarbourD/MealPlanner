from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    quantity = models.CharField(max_length=100)
    item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} {self.item}"
    
    def get_absolute_url(self):
        return reverse('lists_detail', kwargs={'pk': self.id})

class Meal(models.Model):
    week = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    lists = models.ManyToManyField(List)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meal.id': self.id})

