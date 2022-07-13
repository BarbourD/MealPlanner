
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RecipeForm, DirectionsForm
from .models import Meal, List, Photo, Recipe 

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'meal-planner-db'

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def meals_index(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'meals/index.html', {'meals': meals })

def meals_detail(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    recipe_form = RecipeForm()
    directions_form = DirectionsForm()
    lists_meal_doesnt_have = List.objects.exclude(id__in = meal.lists.all().values_list('id'))
    return render(request, 'meals/detail.html', {'meal' : meal, 'recipe_form' : recipe_form, 'directions_form' : directions_form, 'lists' : lists_meal_doesnt_have })

def add_recipe(request, meal_id):
    form = RecipeForm(request.POST)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.meal_id = meal_id
        new_recipe.save()
    return redirect('detail', meal_id=meal_id)
def edit_recipe(request, meal_id):
    form = RecipeForm(request.POST)


def add_directions(request, meal_id):
    form = DirectionsForm(request.POST)
    if form.is_valid():
        new_directions = form.save(commit=False)
        new_directions.meal_id = meal_id
        new_directions.save()
    return redirect('detail', meal_id=meal_id)

def assoc_list(request, meal_id, list_id):
    Meal.objects.get(id=meal_id).lists.remove(list_id)
    return redirect('detail', meal_id=meal_id)

def assoc_list_delete(request, meal_id, list_id):
    Meal.objects.get(id=meal_id).lists.remove(list_id)
    return redirect('detail', meal_id=meal_id)

def add_photo(request, meal_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:                
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, meal_id=meal_id)
            photo.save()
        except Exception as error:
            print('Error uploading photo:', error)
            return redirect('detail', meal_id=meal_id)
        return redirect('detail', meal_id=meal_id)
        
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid Entry = Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['day', 'date', 'name']
    success_url = '/meals/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['day', 'date', 'name']

class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = '/meals/'

class ListList(LoginRequiredMixin, ListView):
    model = List
    template_name = 'lists/index.html'

class ListDetail(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'lists/detail.html'

class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['quantity', 'item']

class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['quantity', 'item']

class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    success_url = '/lists/'

