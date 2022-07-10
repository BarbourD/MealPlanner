from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meals/', views.meals_index, name='index'),
    path('meals/<int:meal_id>/', views.meals_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup')
]