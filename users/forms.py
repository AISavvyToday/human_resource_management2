from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from small_small_hr.models import StaffProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['image']