from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .forms import UserForm, ProfileForm

@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            print profile_form.errors
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
