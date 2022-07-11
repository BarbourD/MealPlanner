from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meals/', views.meals_index, name='index'),
    path('meals/<int:meal_id>/', views.meals_detail, name='detail'),
    path('meals/create', views.MealCreate.as_view(), name='meals_create'),
    path('meals/<int:meal_id>/assoc_list/<int:lsit_id>/', views.assoc_list, name='assoc_spell'),
    path('lists/', views.ListList.as_view(), name='lists_index'),
    path('lists/<int:pk>', views.ListDetail.as_view(), name='lists_detail'),
    path('lists/create', views.ListCreate.as_view(), name='lists_create'),
    path('accounts/signup/', views.signup, name='signup'),
]