from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
from menus.templates import *



# site welcome views (3)
# initial view if no one is logged in
def index(request):
    if 'userid' in request.session:
        return redirect('http://localhost:8000/menus/welcome/')
    return render(request, 'index.html')

# login for returning users
def display_login(request):
    if 'userid' in request.session:
        return redirect('http://localhost:8000/menus/welcome/')
    return render(request, 'login.html')

# login for new users
def display_registration(request):
    if 'userid' in request.session:
        return redirect('http://localhost:8000/menus/welcome/')
    return render(request, 'register.html')


# CRUD
# Create
def create_user(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('http://localhost:8000/register_new/')

    else:
        pw = request.POST['password']
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user_corn = User.objects.create(
            f_name = request.POST['f_name'],
            l_name = request.POST['l_name'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = pw_hash
        )
        return redirect('http://localhost:8000/log_in/')

def login(request):
    users = User.objects.filter(username=request.POST['username'])
    if users:
        logged_user=users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid']=logged_user.id
            return redirect('/menus/welcome')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('/')

    else:
        messages.error(request, 'Username or password is incorrect')
        return redirect('/')

def welcome(request):
    if 'userid' in request.session:
        user_id=request.session['userid']
        logged_user=User.objects.get(id=user_id)
    else:
        return redirect('/')
        
    context = {
        'user': logged_user
    }
    return render(request, 'home.html', context)

def log_out(request):
    request.session.flush()
    return redirect('/')