from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from forms import RegistrationForm
from django.template.context_processors import csrf

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration-complete')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('auth/registration/form.html', token)

def registration_complete(request):
    return render_to_response('auth/registration/complete.html')
