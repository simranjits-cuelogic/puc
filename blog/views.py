from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ArticleForm
from django.views.generic.edit import FormView

from django.views.generic import ListView
from .models import Article

import datetime
from django.views.generic import UpdateView

class ArticleListView(ListView):
    queryset = Article.objects.order_by('-published_on')
    context_object_name = 'article_list'
    template_name = 'blog/article/list.html'

class ArticleView(FormView):
    template_name = 'blog/article/form.html'
    form_class = ArticleForm
    success_url = '/articles'

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
    # if request.method == 'POST':
    article = get_object_or_404(Article, pk=pk)

    article.is_published = not article.is_published
    article.save()
        # Always return and HttpResponseRedirect after succesfully dealing
        # with POST data. This porevents data from being posted twice if a
        # user hits the back button.
    return HttpResponseRedirect(reverse('article_list'))

def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.owner:
        article.delete()

    return HttpResponseRedirect(reverse('article_list'))

class EditArticleView(UpdateView):
    # model = Article
    template_name = 'blog/article/form.html'
    form_class = ArticleForm
    success_url = '/articles'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Article, pk=self.kwargs['pk'])
        # obj = Article.objects.get_or_create(id=self.kwargs['pk'])

        return obj



# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance = request.user)
#         if user_form.is_valid():
#             user_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('home')
#         else:
#             print profile_form.errors
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         form = UserForm(instance=request.user)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
