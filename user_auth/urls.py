from django.conf.urls import url
from . import views as auth_view

# Add this import for session
from django.contrib.auth import views
from user_auth.forms import LoginForm, PasswordForm

urlpatterns = [
    # # root url
    # url(r'^$', views.home, name='home'),
    # url(r'^home/$', views.home, name='home'),

    # Registration URLs
    url(r'^register/$', auth_view.register, name='register'),
    url(r'^registration-complete/$', auth_view.registration_complete,
        name='registration_complete'),

    # Session URLs
    url(r'^login/$', views.login, {
        'template_name': 'auth/session/form.html',
        'authentication_form': LoginForm
        }, name= 'login'),

    url(r'^logout/$', views.logout, {
        'next_page': '/login'
        }, name= 'logout'),

    #Password URLs
    url(r'^forgot-password/$', views.password_reset, {
        'post_reset_redirect' : '/reset-password-requested',
        'template_name': 'auth/password/reset_password_form.html'
        }, name="reset_password"),

    url(r'^reset-password-requested/$', views.password_reset_done, {
        'template_name': 'auth/password/reset_password_requested.html'
        } ),

    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
        views.password_reset_confirm,{
        'template_name': 'auth/password/new_password_form.html',
        'post_reset_redirect': 'password-reset-complete/',
        'set_password_form': PasswordForm
        },
        name='password_reset_confirm'),

    url(r'^password-reset-complete/$',
        views.password_reset_complete, {
        'template_name' : 'auth/password/reset_done'
        },
        name= 'password_reset_complete'),

    url(r'^password-change/$',
        views.password_change, {
        'template_name' : 'auth/password/change_password_form.html'
        },
        name= 'change_password'),

    url(r'^password-change-done/$',
        views.password_change_done, {
        'template_name' : 'auth/password/change_password_done.html'
        },
        name= 'password_change_done'),

]
