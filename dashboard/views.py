from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from blog.models import Article

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "dashboard/home.html")

class LandingView(ListView):
    """
    block of code responsible for showing list of Article's objects
    """
    queryset = Article.objects.all_published()
    context_object_name = 'article_list'
    template_name = 'dashboard/landing.html'
