from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ArticleForm, CommentForm
from django.views.generic.edit import FormView

from django.views.generic import ListView
from .models import Article

import datetime
from django.utils import timezone
from django.views.generic import UpdateView, DetailView

from django.contrib import messages

from django.views import View

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

class ArticleDetailView(DetailView):
    """
    class is responsible for providing object of Article model against corres-
    -ponding pk.
    """
    model = Article
    template_name = 'blog/article/show.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['comment_form'] = CommentForm()
        return context

class CommentView(FormView):
    form_class = CommentForm

    def post(self, request, article_id):

        form = self.form_class(request.POST)
        if form.is_valid():
            # form.save()
            # Need to work here...
            article = get_object_or_404(Article, pk=article_id)
            article.comment_set.create(
                comment = request.POST['comment'],
                article_id = article_id,
                user_id = request.user.id
                )
            messages.success(request, ('Your comment is posted.'))
        else:
            messages.error(request, ('Errro while commenting!'))

        return HttpResponseRedirect(reverse('article', args=[article_id]))
