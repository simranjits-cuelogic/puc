from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField
from django.db.models import Q
import os
# /PROJECT_ROOT/static/blogs/<blog_id>/filename
# image saving path with users ID
def avatar_path(instance, filename):
    return os.path.join('blogs', str(instance.id), filename)

class ArticleQuerySet(models.query.QuerySet):
    """ArticleQuerySet class for all kind of database extraction logic"""

    def all_published(self):
        return self.filter(is_published = True)

    def all_draft(self):
        return self.filter(is_published = False)

class ArticleManager(models.Manager):
    """
    Manager class for Article model to deal with all kind fo database queries.
    """
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def all_published(self):
        return self.get_queryset().all_published()

    def all_draft(self):
        return self.get_queryset().all_draft()

class Article(models.Model):
    title = models.CharField(max_length=150, blank=True)
    desription = models.CharField(max_length=200, blank=True)
    # content = models.TextField(max_length=500, blank=True)
    content = HTMLField()

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

    def all_comments(self):
        return self.comment_set.order_by('-created_on')[:15]

    def comments_count(self):
        return self.comment_set.count()

    def image_url(self):
        """
        Returns the URL of the image associated with this Article.
        If an image hasn't been uploaded yet, it returns a stock image

        :returns: str -- the image url

        """
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/default.jpg'

    @classmethod
    def combine_filter(cls, query):
        return cls.objects.filter(
            Q(title__icontains=query) |
            Q(desription__icontains=query) |
            Q(content__icontains=query)
            )

# Comment's view
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    comment = models.TextField(max_length=500)

    is_deleted = models.BooleanField(default=False)
    deleted_on = models.DateField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.comment[:75] + (self.comment[75:] and '..')
