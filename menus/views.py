from django.shortcuts import render, redirect, HttpResponse
from . models import *
from log_and_reg.models import User
from recipes.models import Recipe
from django.contrib import messages

# function to add tags to a menu
# make sure that the create day function associates with the menu that it belongs to

    # if 'userid' in request.session:
    #     user_id=request.session['userid']
    #     logged_user=User.objects.get(id=user_id)
    # else:
    #     return redirect('/')
# Views to display main app pages
def display_home(request):
    user_id=request.session['userid']
    logged_user=User.objects.get(id=user_id)

    context = {
        'logged_user': logged_user,
        'my_menus': logged_user.menus.all(),
        'my_recipes': logged_user.recipes.all(),
    }
    # write a funciton that pulls the menus that are associated with logged user
    # then write a for loop that finds the
    return render(request, 'home.html', context)

def display_menu_builder(request, menu_id):
    current_menu = Menu.objects.get(id=menu_id)
    days = Day.objects.filter(menu=current_menu)
    # days = current_menu.days.all()
    context = {
        'current_menu': current_menu,
        'days': days
    }
    return render(request, 'menu_builder.html', context)

# Views displaying forms
def new_menu(request):
    return render(request, 'new_menu.html')

def new_tag(request):
    return render(request, 'new_tag.html')


# CRUD commands
# Create
def create_menu(request):
    errors = Menu.objects.menu_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('http://localhost:8000/menus/new')
    else:
        new_menu = Menu.objects.create (
            menu_name = request.POST['menu_name'],
            note = request.POST.get('note'),
            is_public = request.POST.get('is_puclic')
        )
        user_id=request.session['userid']
        logged_user=User.objects.get(id=user_id)
        new_menu.users.add(logged_user)
        
        return redirect('http://localhost:8000/menus/welcome/')

def create_day(request, menu_id):
    current_menu = Menu.objects.get(id=menu_id)
    new_day = Day.objects.create (
        menu = current_menu
    )

    return redirect('menu_builder', menu_id=current_menu.id)

def create_tag(request, menu_id):
    current_menu = Menu.objects.get(id=menu_id)
    new_tag = Tag.objects.create (
        tag_name = request.POST['tag_name']
    )
    new_tag.menus.add(current_menu)

    return redirect('menu_builder', menu_id=current_menu.id)


def edit_menu(request, menu_id):
    current_menu = Menu.objects.get(id=menu_id)
    context = {
        'current_menu': current_menu
    }
    return render(request, 'edit_menu.html', context)

def update_menu(request, menu_id):

    to_update = Menu.objects.get(id=menu_id)

    to_update.menu_name = request.POST['menu_name']
    to_update.note = request.POST['note']
    to_update.is_public = request.POST['is_public']
    to_update.save()

    return redirect('menu_builder', menu_id=to_update.id)

# Read
def get_one_menu(request):
    pass

def get_all_menus(request):
    pass

def get_one_day(request):
    pass

def get_all_days(request):
    pass

def get_one_tag(request):
    pass

def get_all_tags(request):
    pass

# Update
# Delete
def delete_day(request, day_id, menu_id):
    create_menu = Menu.objects.get(id=menu_id)
    to_delete = Day.objects.get(id=day_id)
    to_delete.delete()
    
    return redirect('menu_builder', menu_id=create_menu.id)



# Create your views here.
# menu, day, tag
# menu CRUD:    create, read, update, delete, COPY
# day CRUD:     create, read, update, delete, COPY--- give an alert, saying if you change this it will change all others(if they reuse a component instead of create a copy, give them the option to create a copy instead)
# tag CRUD:     create, read, delete (don't need to update do I???)
