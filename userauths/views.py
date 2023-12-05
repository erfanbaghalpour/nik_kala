from django.http import HttpRequest
from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.views.generic import View
from userauths.models import User
from django.urls import reverse
from django.utils.crypto import get_random_string


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"سلام {username} ، شما به موفقیت ثبت نام شدید.")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context=context)


class RegisterView(View):
    def get(self, request):
        register_form = UserRegisterForm
        context = {
            'form': register_form,
        }
        return render(request, 'userauths/sign-up.html', context=context)

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password1')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                # new_user = User(email=user_email, email_active_code=get_user_model(72), is_active=False,
                #                 username=user_email)
                new_user = User(email=user_email,
                                email_active_code=get_user_model().objects.make_random_password(length=72),
                                is_active=False, username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('userauths:log-in'))
        context = {
            'form': register_form,
        }
        return render(request, 'userauths/sign-up.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = UserRegisterForm
        context = {
            'form': login_form,
        }
        return render(request, 'userauths/log-in.html', context=context)

    def post(self, request):
        pass
