from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class NewUser(forms.Form):
    first_name = forms.CharField(label='Please enter your first name')
    last_name = forms.CharField(label='Please enter your last name')
    username = forms.CharField(label='Please enter username', min_length=8, max_length=30, required=True)
    email = forms.EmailField(label='Please enter your email', required=True)
    password1 = forms.CharField(label='Please enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Please confirm password', widget=forms.PasswordInput)

    def valid_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is taken")
        return username

    def valid_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Someone has already used this email to sign up")
        return email

    def valid_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password2 != password1:
            raise ValidationError("The passwords were not a match")

        return password1

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.changed_data['password2'],
                                        first_name=self.cleaned_data['first_name'],
                                        last_name=self.cleaned_data['last_name'])




