from django.conf.urls import url
from . import views as auth_view

# Add this import for session
from django.contrib.auth import views
from user_auth.forms import LoginForm

urlpatterns = [
    # # root url
    # url(r'^$', views.home, name='home'),
    # url(r'^home/$', views.home, name='home'),

    # Registration URLs
    url(r'^register/$', auth_view.register, name='register'),
    url(r'^registration-complete/$', auth_view.registration_complete,
        name='registration_complete'),

    url(r'^login/$', views.login, {
        'template_name': 'auth/session/form.html', 'authentication_form': LoginForm
        }, name= 'login'),

    url(r'^logout/$', views.logout, {'next_page': '/login'}, name= 'logout'),
]
