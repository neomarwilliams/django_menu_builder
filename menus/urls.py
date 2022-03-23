from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_menu),
    path('<int:menu_id>/', views.display_one_menu),
    path('day/create/<int:menu_id>/', views.create_day),
    path('<int:menu_id>/day/delete/<int:day_id>/', views.delete_day),
    path('menu_builder/<int:menu_id>/', views.display_menu_builder, name='menu_builder'),
    path('menu_builder/<int:menu_id>/<int:meal_type_id>/<int:day_id>/', views.display_menu_builder_with_cards, name='menu_builder_with_cards'),
    path('new/', views.new_menu, name='new_menu'),
    path('welcome/', views.display_home, name='welcome'),
    path('edit/<int:menu_id>/', views.edit_menu),
    path('update/<int:menu_id>/', views.update_menu),
    path('delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    # path('new/tags/', views.new_tag),
]