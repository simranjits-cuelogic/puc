from django.contrib import admin
from .models import Article, Comment

from django.core.urlresolvers import resolve

class ArticleInline(admin.TabularInline):
    model = Comment
    extra = 0
    fieldsets = [
        (None,               {'fields': ['comment', 'user']}),
    ]
    # readonly_fields = ('comment',)

    def has_add_permission(self, request):
        return resolve(request.path_info).url_name == 'blog_article_change'

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'desription']}),
        ('Article information', {'fields': ['content']}),
    ]

    list_display = ('titlized_title', 'is_published', 'is_drafted', 'is_deleted')
    list_filter = ['title', 'is_published']
    search_fields = ['title', 'content', 'desription']

    inlines = [ArticleInline]

    def titlized_title(self, obj):
        return obj.title.upper()
    titlized_title.short_description = 'article titlte'



admin.site.register(Article, ArticleAdmin)
