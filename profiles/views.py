from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import UserForm, ProfileForm

@transaction.atomic
def update_profile(request):
    """
    this block of code used to update the user information along with it's profile,
    since we have different models for user and it's profile. That's why using
    two form instance name 'user_form' and 'profile_form'. After sucessfully
    validating user_form and profile_form given data is being saved and sucess
    message is genrated and request is being redirected to landing page and in
    case of errors in forms redirecting to same url with errors embedded in it.
    Above execution being done in case of POST type of request. If request is
    type of GET, simply show the blank forms (user_form, profile_form).
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
