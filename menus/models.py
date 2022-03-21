from django.db import models

class TagManager(models.Manager):
    def tag_validator(self, postData):
        errors = {}
        if len(postData['tag_name']) < 2:
            errors['tag_name'] = "Tag name must have 2 or more characters"
        
        return errors

class Tag(models.Model):
    tag_name = models.CharField(max_length=45)


class MenuManager(models.Manager):
    def menu_validator(self, postData):
        
        errors = {}
        # CHECK THE NEXT TWO LINES make sure to set this up so it is only searching the USERS menu names
        # name_check = Menu.objects.filter(name=postData['name'])
        # if name_check:
        #     errors['duplicate_menu_name']= 'You already have  menu with this name'
        # for menu in Menu.objects.all():
        #     if postData['name'] == menu.name:
        #         errors['duplicate_menu_name']= 'You already have  menu with this name'
        if len(postData['menu_name']) < 1:
            errors['name'] = 'menu name is required'


        return errors

class Menu(models.Model):
    menu_name = models.CharField(max_length=45)
    note = models.CharField(max_length=255, null=True)
    is_public = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='menus')
    objects = MenuManager()





class Day(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)



