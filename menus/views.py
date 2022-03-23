from django.shortcuts import render, redirect, HttpResponse
from . models import *
from log_and_reg.models import User
from recipes.models import Recipe, MealType
from django.contrib import messages

# CRUD commands for menus, and day objects
# CRUD commands for tags are commented out at the bottom of the page


# Create
# Adds new menu object (acts as frame for day objects)
def create_menu(request):

    if 'userid' not in request.session:
        return redirect('/')

    errors = Menu.objects.menu_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('http://localhost:8000/menus/new')
    else:
        public_boolean = False
        if(request.POST.get('is_public') == 1):
            public_boolean = True
        new_menu = Menu.objects.create (
            menu_name = request.POST['menu_name'],
            note = request.POST.get('note'),
            is_public = public_boolean,
        )
        user_id=request.session['userid']
        logged_user=User.objects.get(id=user_id)
        new_menu.users.add(logged_user)
        
        return redirect('http://localhost:8000/menus/welcome/')

# Adds new day object to menu
def create_day(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    new_day = Day.objects.create (
        menu = current_menu
    )

    return redirect('menu_builder', menu_id=current_menu.id)


# Read
# shows home page
def display_home(request):

    if 'userid' not in request.session:
        return redirect('/')

    user_id=request.session['userid']
    logged_user=User.objects.get(id=user_id)

    context = {
        'logged_user': logged_user,
        'my_menus': logged_user.menus.all(),
        'my_recipes': logged_user.recipes.all(),

    }

    return render(request, 'home.html', context)

# shows menu builder dashboard page
def display_menu_builder_with_cards(request, menu_id, meal_type_id, day_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    days = Day.objects.filter(menu=current_menu)
    current_day = Day.objects.get(id=day_id)
    current_meal = MealType.objects.get(id=meal_type_id)

    recipes_by_day = current_day.recipes.all()
    recipe_tab_list = {}

    # make a list of all of the mealtypes assigned to a day. 
    for day in days:
        meals_of_day = day.meals.all()
        for meal_type in meals_of_day:
            recipe_list = []
            for recipe in recipes_by_day:
                recipe_sorter = recipe.meals.all()
                for meal in recipe_sorter:
                    if meal.id == meal_type.id:
                        recipe_list.append(recipe)
            recipe_tab_list['meal_type.meal_name'] = recipe_list
    
    meals_of_day = current_day.meals.all()
    
    for recipe in recipes_by_day:
        # print(recipe)
        recipe_sorter = recipe.meals.all()
        # print(recipe_sorter)
        for meal in recipe_sorter:
            # print(meal.id)
            # print(meal_type_id)
            if meal.id == meal_type_id: 
                recipe_tab_list.append(recipe)
    # days = current_menu.days.all()

    recipe_list = []
    for recipe in recipe_tab_list:
        print(recipe.title)
        recipe_list.append(recipe.title)

    print('WORKING HERE')
    print(recipe_list)
    context = {
        'current_menu': current_menu,
        'recipe_tab': recipe_tab_list,
        'recipe_list': recipe_list,
        'days': days,
    }

    return render(request, 'menu_builder.html', context)

def display_menu_builder(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    days = Day.objects.filter(menu=current_menu)
    # days = current_menu.days.all()

    whole_menu_tab_list = []
    day_tab_list = []

    # ugh this is the worst 
    # make a list of all of the mealtypes assigned to a day. 
    for day in days:
        meals_of_day = day.meals.all()
        recipes_of_day = day.recipes.all()
        for meal_type in meals_of_day:
            recipe_list = []
            for recipe in recipes_of_day:
                recipe_sorter = recipe.meals.all()
                for meal in recipe_sorter:
                    if meal.id == meal_type.id:
                        recipe_list.append(recipe)
            
            # (I can just put the labels on the cards from the day. no prob)
            # print(meal_type.meal_name)
            # print(recipe_list)
            day_tab_list.append(recipe_list)
            print('ONE DAY HERE')
            print(day_tab_list)
        whole_menu_tab_list.append(day_tab_list)


    print('WHOLE MENU')
    print(whole_menu_tab_list)
    context = {
        'current_menu': current_menu,
        'days': days, 
        'whole_menu_tab_list': whole_menu_tab_list,
    }
    return render(request, 'menu_builder.html', context)

# shows new menu form page
def new_menu(request):

    if 'userid' not in request.session:
        return redirect('/')

    return render(request, 'new_menu.html')

# shows one menu with details on page
def display_one_menu(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    days = Day.objects.filter(menu=current_menu)

    context = {
        'current_menu': current_menu,
        'days': days
    }

    return render(request, 'one_menu.html', context)


# Update
# displays edit form, prepopulated with current field values
def edit_menu(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    context = {
        'current_menu': current_menu
    }
    return render(request, 'edit_menu.html', context)

# updates values in menu edit form
def update_menu(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    to_update = Menu.objects.get(id=menu_id)

    public_boolean = False
    if(request.POST.get('is_public') == 1):
        public_boolean = True

    to_update.menu_name = request.POST['menu_name']
    to_update.note = request.POST['note']
    to_update.is_public = public_boolean
    to_update.save()

    return redirect('menu_builder', menu_id=to_update.id)


# Delete
def delete_day(request, day_id, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    current_menu = Menu.objects.get(id=menu_id)
    to_delete = Day.objects.get(id=day_id)
    to_delete.delete()
    
    return redirect('menu_builder', menu_id=current_menu.id)

def delete_menu(request, menu_id):

    if 'userid' not in request.session:
        return redirect('/')

    menu_to_delete = Menu.objects.get(id=menu_id)
    menu_to_delete.delete()

    return redirect('welcome')



# In progress
# Tag Functionality-- create new tag (to be added later)
# def create_tag(request, menu_id):
#     current_menu = Menu.objects.get(id=menu_id)
#     new_tag = Tag.objects.create (
#         tag_name = request.POST['tag_name']
#     )
#     new_tag.menus.add(current_menu)

#     return redirect('menu_builder', menu_id=current_menu.id)


# Tag functionality-- display tag form (to be added later)
# def new_tag(request):
#     return render(request, 'new_tag.html')
