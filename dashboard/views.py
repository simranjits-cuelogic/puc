from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "dashboard/home.html")
