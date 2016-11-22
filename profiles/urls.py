from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^settings/$', login_required(views.update_profile), name='settings'),
]
