from django.db import models
from django.contrib.auth.models import User
# no need to create a user model as it's inbuilt in Django

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # associating user with model, one user = one profile; on deleting the user, the profile will also be deleted
    image = models.ImageField(default='profilepic.png', upload_to='profile_pic')
    # needs to install "pip install pillow" for ImageField
    location = models.CharField(max_length=100)
    favorite_base_spirits = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
        # what returns by default when we call the model i.e., in this case it will be a list of usernames of all objects

# once model's set up, do the migration