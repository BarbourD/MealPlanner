from django.contrib import admin
from .models import Meal, Recipe, List

# Register your models here.

admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(List)
