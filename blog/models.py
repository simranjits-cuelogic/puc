from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField

import os
# /PROJECT_ROOT/static/blogs/<blog_id>/filename
# image saving path with users ID
def avatar_path(instance, filename):
    return os.path.join('static/blogs', str(instance.id), filename)

class ArticleQuerySet(models.query.QuerySet):
    """ArticleQuerySet class for all kind of database extraction logic"""

    def all_published(self):
        return self.filter(is_published = True)

class ArticleManager(models.Manager):
    """
    Manager class for Article model to deal with all kind fo database queries.
    """
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def all_published(self):
        return self.get_queryset().all_published()

class Article(models.Model):
    title = models.CharField(max_length=30, blank=True)
    # content = models.TextField(max_length=500, blank=True)
    content = RichTextField()

    is_drafted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now_add = True)

    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    objects = ArticleManager()
    # all_published = Article.objects.all_published()

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
