from django.conf.urls import url
from .views import ArticleView, ArticleListView

from . import views

urlpatterns = [
    url(r'articles/$', ArticleListView.as_view(), name='article_list'),
    url(r'article/add/$', ArticleView.as_view(), name='add_article'),
    url(r'article/(?P<pk>[0-9]+)/publish-unpublish/$', views.publish_unpublish, name='publish_unpublish'),
    url(r'article/(?P<pk>[0-9]+)/delete/$', views.delete, name='article_delete'),

#     url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
]
