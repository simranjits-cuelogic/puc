from django.conf.urls import url
from . import views

urlpatterns = [
    # # root url
    # url(r'^$', views.home, name='home'),
    # url(r'^home/$', views.home, name='home'),

    # Registration URLs
    url(r'^register/$', views.register, name='register'),
    url(r'^registration-complete/$', views.registration_complete,
        name='registration_complete'),
]
