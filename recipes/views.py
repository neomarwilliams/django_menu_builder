from django.shortcuts import render, redirect, HttpResponse
from .models import *
from menus.models import Menu, Day
from log_and_reg.models import User
from django.contrib import messages
import bcrypt

    # if 'userid' in request.session:
    #     user_id=request.session['userid']
    #     logged_user=User.objects.get(id=user_id)
    # else:
    #     return redirect('/')

# site welcome views (3)
# initial view if no one is logged in
def recipes(request, menu_id, day_id):
    current_menu = Menu.objects.get(id=menu_id)
    current_day = Day.objects.get(id=day_id)

    context = {
        'current_day': current_day,
        'current_menu': current_menu,
    }
    return render(request, 'new_recipe.html', context)

def create_recipe(request, day_id, menu_id):
    errors = Recipe.objects.recipe_validator(request.POST)

    if 'userid' in request.session:
        user_id=request.session['userid']
        logged_user=User.objects.get(id=user_id)
    
    else:
        return redirect('log_in')
    # user_id=request.session['userid']

    # logged_user=User.objects.get(id=user_id)
    current_menu = Menu.objects.get(id = menu_id)
    current_day=Day.objects.get(id = day_id)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('new_recipe', menu_id = current_menu.id, day_id = current_day.id)

    else:

        new_recipe=Recipe.objects.create(
            title = request.POST.get('title'),
            link = request.POST.get('link'),
        )

        new_recipe.days.add(current_day)
        new_recipe.recipe_types.add(request.POST['recipe_type'])
        new_recipe.users.add(logged_user)
        new_recipe.meals.add(request.POST['meal'])

        return redirect('menu_builder', menu_id=current_menu.id)

def delete_recipe(request, day_id, menu_id, recipe_id):
    current_menu = Menu.objects.get(id=menu_id)
    current_day = Day.objects.get(id=day_id)
    recipe_to_delete = current_day.recipes.get(id=recipe_id)
    recipe_to_delete.delete()

    return redirect('menu_builder', menu_id=current_menu.id)


# def delete_day(request, day_id, menu_id):
#     current_menu = Menu.objects.get(id=menu_id)
#     to_delete = Day.objects.get(id=day_id)
#     to_delete.delete()
    
#     return redirect('menu_builder', menu_id=current_menu.id)
# Create your views here.
# recipe, recipe type, photo
# recipe CRUD           create, read, update, delete
# recipe type CRUD      create, read, update, delete
# photo CRUD            create, read, update, delete
