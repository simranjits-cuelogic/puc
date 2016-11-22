from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^dashboard/$', views.home, name='home'),
    url(r'^$', views.landing, name='landing'),
]
