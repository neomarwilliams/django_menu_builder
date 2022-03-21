from django.db import models
from menus.models import Menu
from recipes.models import Recipe
import re
import bcrypt

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')
        users = User.objects.all()
        email_check = User.objects.filter(email=postData['email'])
        username_check = User.objects.filter(username=postData['username'])
        if email_check:
            errors['duplicate_email']='This email is already in use'
        if username_check:
            errors['duplicate_username']='This username is taken'
        if len(postData['f_name']) < 2:
            errors['f_name'] = 'First name must be at least 2 characters.'
        if len(postData['l_name']) < 2:
            errors['l_name'] = 'Last name must be at least 2 characters.'
        if len(postData['username']) < 2:
            errors['username'] = 'Username must be at least 2 characters.'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please provide a valid email adress.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if not postData['password'] == postData['conf_password']:
            errors['pw_not_match'] = 'Passwords do not match'

        return errors

class User(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menus = models.ManyToManyField(Menu, related_name='users')
    recipes = models.ManyToManyField(Recipe, related_name='users')
    objects = UserManager()
