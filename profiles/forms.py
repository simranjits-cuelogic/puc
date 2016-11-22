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
        fields = ('bio', 'location', 'birth_date', 'avatar',)

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

    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']

    #     try:
    #         w, h = get_image_dimensions(avatar)

    #         #validate dimensions
    #         max_width = max_height = 100
    #         if w > max_width or h > max_height:
    #             raise forms.ValidationError(
    #                 u'Please use an image that is '
    #                  '%s x %s pixels or smaller.' % (max_width, max_height))

    #         #validate content type
    #         main, sub = avatar.content_type.split('/')
    #         if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #             raise forms.ValidationError(u'Please use a JPEG, '
    #                 'GIF or PNG image.')

    #         #validate file size
    #         if len(avatar) > (20 * 1024):
    #             raise forms.ValidationError(
    #                 u'Avatar file size may not exceed 20k.')

    #     except AttributeError:
    #         """
    #         Handles case when we are updating the user profile
    #         and do not supply a new avatar
    #         """
    #         pass

    #     return avatar
