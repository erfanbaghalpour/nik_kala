from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانواگی', max_length=300,
                                error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                                                'max_length': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کارکتر باشد'},
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                              'placeholder': 'نام و نام خانوادگی'}))
    email = forms.EmailField(label='ایمیل', max_length=300,
                             widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg',
                                                            'placeholder': 'ایمیل'}),
                             error_messages={'required': 'لطفاایمیل خود را وارد کنید'})
    title = forms.CharField(label='عنوان', max_length=300,
                            error_messages={'required': 'لطفا عنوان پیام خود را وارد کنید',
                                            'max_length': 'عنوان نمیتواند بیشتر از 300 کارکتر باشد'},
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                          'placeholder': 'عنوان'}))
    message = forms.CharField(label='پیام', max_length=2000,
                              widget=forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                                           'placeholder': 'پیام'}),
                              error_messages={'required': 'لطفا پیام خود را وارد کنید',
                                              'max_length': 'پیام شما نمیتواند بیشتر از 2000 کارکتر باشد'})


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        max_length = {
            'full_name': 50,
            'email': 300,
            'title': 400,
            'message': 1000,
        }
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                            'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                            'placeholder': 'عنوان'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-lg',
                                             'placeholder': 'پیام'}),
        }
        # labels = {
        #     'full_name'
        # }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کارکتر باشد'
            },
            'email': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'ایمیل نمیتواند بیشتر از 300 کارکتر باشد'
            },
            'title': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'عنوان نمیتواند بیشتر از 400 کارکتر باشد'
            },
            'message': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'پیام نمیتواند بیشتر از 1000 کارکتر باشد'
            },

        }
