from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
# /PROJECT_ROOT/photos/<user_id>/filename
# image saving path with users ID
def avatar_path(instance, filename):
    return os.path.join('static/avatars', str(instance.id), filename)


class Profile(models.Model):
    """docstring for Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    avatar = models.ImageField(
        'profile picture',
        upload_to = avatar_path, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

