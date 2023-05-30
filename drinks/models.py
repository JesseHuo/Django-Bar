from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# import inbuild user model of Django

# Create your models here. models are the blueprint which can be used to create database tables


class Item(models.Model):
# inherited from models.Model in django.db
    def __str__(self):
        return self.item_name
    # formats the output when query for all objects
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(default="mixing.png", upload_to='drinks_pic')
    item_ingredients = models.CharField(max_length=400, default="TBU")
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    # added a foreign key that belongs to the user mode and establishes connection between User & Item
    # when adding a field to model that already has objects in it, need to set a default value for the existing objects
    # on_delete options: CASCADE: when the referenced object is deleted, also delete the objects that have refereces to it. e.g., when a post is deleted, all comments will be gone with it

# after making changes to this class, you need to convay the change to Django
# 1. "python manage.py makemigrations drinks" will create a migration file captures all changes
# 2. "python manage.py sqlmigrate drinks 0001" 0001 is from the returned info from last one; this will create the table, or upgrade the table structure to the latest 
# then migrate again with "python manage.py migrate"

# use python shell to edit table

# -------------use the "--fake" to avoid conflect error---------------------------
# 1. manage.py makemigrations -> 2. manage.py migrate --fake  -> 3. make change -> 4. manage.py make migrations -> 5.manage.py migrate
# using "--fake" can avoid having conflict error

# ------------if a table is not created during model migration can also use fake to unapply the migration------------
# 1. python manage.py migrate --fake APPNAME zero;  2.python manage.py migrate APPNAME;  3. python manage.py sqlmigrate APPNAME 0001


    def get_absolute_url(self):
        return reverse('drinks:detail', kwargs={'pk': self.pk})
    # when a new item is created, we want to redirect to detail view of that item
    # self's pk is passed into the url 