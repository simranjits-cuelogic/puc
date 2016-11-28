from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ArticleForm
from django.views.generic.edit import FormView

from django.views.generic import ListView
from .models import Article

import datetime
from django.views.generic import UpdateView

from django.contrib import messages

articles_url = '/articles'
class ArticleListView(ListView):
    """
    block of code responsible for showing list of Article's objects
    """
    queryset = Article.objects.order_by('-published_on')
    context_object_name = 'article_list'
    template_name = 'blog/article/list.html'

class ArticleView(FormView):
    """
    block of code responsible for adding new Artcle.
    """
    template_name = 'blog/article/add.html'
    form_class = ArticleForm
    success_url = articles_url

    def form_valid(self, form):
        is_published = False
        if 'publish' in self.request.POST:
            is_published = True

        Article.objects.create(
            title = form.cleaned_data['title'],
            content = form.cleaned_data['content'],
            is_published = is_published,
            owner = self.request.user
        )
        return super(ArticleView, self).form_valid(form)

def publish_unpublish(request, pk):
    """
    block of code responsible for publish and draft the article.
    """
    article = get_object_or_404(Article, pk=pk)

    article.is_published = not article.is_published
    article.save()
    print article.publish_status

    return HttpResponseRedirect(articles_url)

def delete(request, pk):
    """
    block of code responsible for deletion of article.
    """
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.owner:
        article.delete()
        messages.success(request, ('Your article is deleted now!'))
    else:
        messages.error(request, ('You are not authorized to delete this.'))

    return HttpResponseRedirect(articles_url)

class EditArticleView(UpdateView):
    """
    class is responsible for update the articles
    """
    model = Article
    template_name = 'blog/article/edit.html'
    form_class = ArticleForm
    success_url = articles_url
