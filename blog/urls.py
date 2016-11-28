from django.conf.urls import url
from .views import (
    ArticleView, ArticleListView, EditArticleView, ArticleDetailView
    )
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'articles/$', login_required(ArticleListView.as_view()), name='article_list'),
    url(r'article/add/$', ArticleView.as_view(), name='add_article'),
    url(r'article/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article'),
    url(r'article/(?P<pk>[0-9]+)/publish-unpublish/$', views.publish_unpublish, name='publish_unpublish'),
    url(r'article/(?P<pk>[0-9]+)/delete/$', views.delete, name='article_delete'),
    url(r'article/(?P<pk>\d+)/edit/$', EditArticleView.as_view(), name="edit-article"),
]
