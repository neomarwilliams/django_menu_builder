from django.urls import path
from . import views

urlpatterns = [
    # path('', views.recipes),
    path('new/<int:menu_id>/<int:day_id>/', views.recipes, name = 'new_recipe'),
    path('create/<int:menu_id>/<int:day_id>/', views.create_recipe),
    path('delete/<int:menu_id>/<int:day_id>/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]