from django.conf.urls import url
from . import views
from .views import LandingView

# We are adding a URL called /home
urlpatterns = [
    url(r'^dashboard/$', views.home, name='home'),
    url(r'^$', LandingView.as_view(), name='landing'),
]
