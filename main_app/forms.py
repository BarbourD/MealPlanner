from django.forms import ModelForm
from .models import Recipe, Directions
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['ingredients']


class DirectionsForm(ModelForm):
    directions = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Directions
        fields = ['directions']

