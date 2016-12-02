from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from nocaptcha_recaptcha.fields import NoReCaptchaField

# login
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("Password fields didn't match with each other."),
    }

    username = forms.CharField(label='Username', max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'name' : 'username'}))

    email = forms.EmailField(label='Email', max_length=30, required=True,
        widget=forms.EmailInput(attrs={'class' : 'form-control', 'name' : 'email'}))

    password1 = forms.CharField(label="Password", max_length=30, required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'name' : 'password1'}))

    password2 = forms.CharField(label="Password Confirmation", max_length=30, required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'name' : 'password2'}),
        help_text= ("Enter the same password as above, for verification."))

    # captcha = NoReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def clean(self):
        # call upper class clean method to get all the default functionalities
        cleaned_data = super(LoginForm, self).clean()

        if not cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)

class PasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Password", max_length=30, required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'name' : 'password1'}))

    new_password2 = forms.CharField(label="Password Confirmation", max_length=30, required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control', 'name' : 'password2'}),
        help_text= ("Enter the same password as above, for verification."))

class ChangePasswordForm(PasswordChangeForm):
        error_css_class = 'has-error'
        error_messages = {'password_incorrect':
                  "Invalid"}
        old_password = forms.CharField(required=True, label='Old Password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Old password is must.'})

        new_password1 = forms.CharField(required=True, label='New Password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Old password is must.'})
        new_password2 = forms.CharField(required=True, label='New Passowrd Confirmation',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Old password is must.'})
