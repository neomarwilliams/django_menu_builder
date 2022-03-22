from django.shortcuts import render, redirect, HttpResponse
from .models import *
from menus.models import Menu, Day
from log_and_reg.models import User
from django.contrib import messages
import bcrypt


def recipes(request, menu_id, day_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    current_day = Day.objects.get(id=day_id)

    context = {
        'current_day': current_day,
        'current_menu': current_menu,
    }
    return render(request, 'new_recipe.html', context)

def create_recipe(request, day_id, menu_id):

    if 'userid' not in request.session:
        return redirect('/')


    logged_user=User.objects.get(id=user_id)
    current_menu = Menu.objects.get(id = menu_id)
    current_day=Day.objects.get(id = day_id)
    errors = Recipe.objects.recipe_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('new_recipe', menu_id = current_menu.id, day_id = current_day.id)

    else:
        meal_type = request.POST.get('meal')
        new_recipe=Recipe.objects.create(
            title = request.POST.get('title'),
            link = request.POST.get('link'),
        )

        new_recipe.days.add(current_day)
        new_recipe.recipe_types.add(request.POST['recipe_type'])
        new_recipe.users.add(logged_user)
        new_recipe.meals.add(request.POST['meal'])
        new_recipe.menus.add(current_menu)
        current_day.meals.add(meal_type)
        

        return redirect('menu_builder', menu_id=current_menu.id)

def delete_recipe(request, day_id, menu_id, recipe_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    current_day = Day.objects.get(id=day_id)
    recipe_to_delete = current_day.recipes.get(id=recipe_id)
    recipe_to_delete.delete()

    return redirect('menu_builder', menu_id=current_menu.id)


def card_tab_display(request, menu_id, day_id, meal_type_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    current_day = Day.objects.get(id=day_id)

    Recipe.objects.filter(meals=meal_type_id)
    
    # days = Day.objects.filter(menu=current_menu)
    recipes_by_day = current_day.recipes.all()
    recipe_tab = {}

    for recipe in recipes_by_day:
        recipe_sorter = recipe.meals.all()
        for meal in recipe_sorter:
            if meal == meal_type_id:
                recipe_tab['recipe'] = recipe
                print(recipe_tab)
        
        return recipe_tab
    
    # recipes_by_day.objects.filter(meal_type_id=meal_type_id)


    context = {
        'current_menu': current_menu,
        # 'days': days,
        'recipe_tab' : recipe_tab,
    }
    return render(request, 'menu_builder.html', context)


