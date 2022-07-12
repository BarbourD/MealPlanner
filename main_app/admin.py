from django.contrib import admin
from .models import Meal, Recipe, Photo, List

# Register your models here.

admin.site.register(Meal)
admin.site.register(Recipe)

admin.site.register(List)
admin.site.register(Photo)
