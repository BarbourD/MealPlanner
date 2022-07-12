
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RecipeForm

from .models import Meal, List 

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
    return render(request, 'meals/detail.html', {'meal' : meal })

def add_recipe(request, meal_id):
    form = RecipeForm(request.POST)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.meal_id = meal_id
        new_recipe.save()
    return redirect('detail', meal_id=meal_id)

def assoc_list(request, meal_id, list_id):
    Meal.objects.get(id=meal_id).lists.remove(list_id)
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
    

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class ListList(LoginRequiredMixin, ListView):
    model = List
    template_name = 'lists/index.html'

class ListDetail(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'lists/detail.html'

class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['quantity', 'item']
