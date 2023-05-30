from django.db.models.signals import post_save
# get signal when form.save() is executed
from django.contrib.auth.models import User
# form is saved for specific user
from django.dispatch import receiver
# to receive the signal 
from .models import Profile


@receiver(post_save, sender=User)
# function called when a sender (User) post a save
def build_profile(sender, instance, created, **kwargs):
    # instance is the user saved here. the function is triggered by .save(), created is a boolem for checking if the user is created when save()
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
    # user profile is saved


