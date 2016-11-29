from django.contrib import admin

from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article)
