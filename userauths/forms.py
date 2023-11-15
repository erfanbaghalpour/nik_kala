from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from userauths.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "نام کاربری"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ایمیل"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": " کلمه عبور"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "تکرار کلمه عبور "}))
    remember_me = forms.BooleanField(widget=forms.CheckboxInput)

    class Meta:
        model = User
        fields = ['username', 'email']
