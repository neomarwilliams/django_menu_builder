from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_menu),
    path('day/create/<int:menu_id>/', views.create_day),
    path('<int:menu_id>/day/delete/<int:day_id>/', views.delete_day),
    # path('menu_builder/', views.display_menu_builder),
    path('menu_builder/<int:menu_id>/', views.display_menu_builder, name='menu_builder'),
    path('new/', views.new_menu, name='new_menu'),
    path('new/tags/', views.new_tag),
    path('welcome/', views.display_home, name='welcome'),
    path('edit/<int:menu_id>/', views.edit_menu),
    path('update/<int:menu_id>/', views.update_menu),

    # path('', include(log_and_reg.urls)),
    # path('menus/', include(menus.urls)),
    # path('recipes/', include(recipes.urls)),
]