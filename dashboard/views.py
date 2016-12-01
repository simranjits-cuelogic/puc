from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from blog.models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "dashboard/home.html")

class LandingView(ListView):
    """
    block of code responsible for showing list of Article's objects
    """
    context_object_name = 'article_list'
    template_name = 'dashboard/landing.html'
    queryset = Article.objects.all_published()

    def get_queryset(self):
        queryset = super(LandingView, self).get_queryset()

        # Get the q GET parameter
        query = self.request.GET.get('q')
        # query = query.replace(" ","+")
        if query is None:
            return queryset

        queryset = Article.combine_filter(query)
        return queryset
