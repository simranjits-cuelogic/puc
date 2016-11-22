from django import forms
from django.contrib.auth.models import User
from .models import Profile

from django.views.generic.edit import UpdateView

BIRTH_YEAR_CHOICES = range(1990, 2016)
LOCATIONS = (
    ('in', 'India'),
    ('pk', 'Pakistan'),
    ('ca', 'Canada'),
    ('usa', 'Amarica'),
)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ('email', 'first_name', 'last_name', 'username',)
        fields = ('first_name', 'last_name',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date',)

    birth_date = forms.DateField(
        label = "Date of Birth",
        required = True,
        widget = forms.SelectDateWidget(
            years = BIRTH_YEAR_CHOICES)
        )

    location = forms.ChoiceField(
        choices = LOCATIONS,
        label = "Country",
        initial = 'Please select',
        widget = forms.Select(),
        required = True
        )
