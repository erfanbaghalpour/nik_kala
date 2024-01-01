from django import forms
from userauths.models import User


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
