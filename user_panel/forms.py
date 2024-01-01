from django import forms
from userauths.models import User
from django.core import validators
from django.core.exceptions import ValidationError


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile', 'address', 'email', 'about_user', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                # 'class': 'form-label form-label form-control-lg'
                # 'class': 'personal-info',
                'class': 'form-control',

            }),
            'last_name': forms.TextInput(attrs={
                # 'class': 'form-label form-label form-control-lg'
                # 'class': 'personal-info',
                'class': 'form-control',

            }),
            'mobile': forms.TextInput(attrs={
                # 'class': 'form-label form-label form-control-lg'
                # 'class': 'personal-info',
                'class': 'form-control',

            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                # 'class': 'form-label form-label form-control-lg',
                # 'class': 'personal-info',
                'class': 'form-control',

                'rows': 3,
                'id': 'message'
            }),
            'about_user': forms.Textarea(attrs={
                # 'class': 'form-label form-label form-control-lg',
                # 'class': 'personal-info',
                'class': 'form-control',

                'rows': 3,
                'id': 'message'
            }),
            'email': forms.EmailInput(attrs={
                # 'class': 'form-label form-label form-control-lg'
                # 'class': 'personal-info',
                'class': 'form-control',

            }),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'mobile': 'شماره تماس',
            'address': 'آدرس',
            'about_user': 'درباره شخص',
            'email': 'ایمیل',
            'image': 'تصویر کاربر',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
