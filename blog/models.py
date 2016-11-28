from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField

import os
# /PROJECT_ROOT/static/blogs/<blog_id>/filename
# image saving path with users ID
def avatar_path(instance, filename):
    return os.path.join('static/blogs', str(instance.id), filename)

class Article(models.Model):
    title = models.CharField(max_length=30, blank=True)
    # content = models.TextField(max_length=500, blank=True)
    content = RichTextField()

    is_drafted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now_add = True)

    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    image = models.ImageField(
        'profile picture',
        upload_to = avatar_path, null=True)

    def __str__(self):
        return self.title

    def publish_status(self):
        status = 'Drafted'
        if self.is_published:
            status = 'Published'

        return status

    def publish_status_action(self):
        status = 'Unpublish'
        if not self.is_published:
            status = 'Publish'

        return status


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    comment = models.TextField(max_length=200)

    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateField(null=True, blank=True)
