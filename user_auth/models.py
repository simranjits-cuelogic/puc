from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User as AuthUser

class User(AuthUser):

    class Meta:
        proxy = True

    def total_articles(self):
        return self.article_set

    def published_articles(self):
        return self.article_set.all_published()

    def draft_articles(self):
        return self.article_set.all_draft()
