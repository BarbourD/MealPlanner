from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meals/', views.meals_index, name='index'),
    path('meals/<int:meal_id>/', views.meals_detail, name='detail'),
    path('meals/create', views.MealCreate.as_view(), name='meals_create'),
    path('meals/<int:pk>/update', views.MealUpdate.as_view(), name='meals_update'),
    path('meals/<int:pk>/delete', views.MealDelete.as_view(), name='meals_delete'),
    
    path('meals/<int:meal_id>/add_recipe/', views.add_recipe, name='add_recipe'),
    path('meals/<int:meal_id>/add_directions/', views.add_directions, name='add_directions'),
    
    path('meals/<int:meal_id>/assoc_list/<int:list_id>/', views.assoc_list, name='assoc_list'),
    path('meals/<int:meal_id>/assoc_list/<int:list_id>/delete/', views.assoc_list_delete, name='assoc_list_delete'),
    
    path('lists/', views.ListList.as_view(), name='lists_index'),
    path('lists/<int:pk>/', views.ListDetail.as_view(), name='lists_detail'),
    path('lists/create', views.ListCreate.as_view(), name='lists_create'),
    path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete'),
    
    path('meals/<int:meal_id>/add_photo/', views.add_photo, name='add_photo'),
    
    path('accounts/signup/', views.signup, name='signup'),
]