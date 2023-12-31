from django.http import HttpRequest
from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm, UserLoginForm, UserForgetPasswordForm, UserResetPasswordForm
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib import messages
from django.views.generic import View
from userauths.models import User
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.http import Http404
from django.conf import settings
from utils.email_service import send_email


# Userr = settings.AUTH_USER_MODEL


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
                new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                username=user_email)
                # new_user = User(email=user_email,
                #                 email_active_code=get_user_model().objects.make_random_password(length=72),
                #                 is_active=False, username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/active_account.html')
                return redirect(reverse('userauths:log-in'))
        context = {
            'form': register_form,
        }
        return render(request, 'userauths/sign-up.html', context=context)


def login_view(request: HttpRequest):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email_log')
            user_pass = login_form.cleaned_data.get('password_log')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email_log', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('core:index'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
    else:
        login_form = UserLoginForm()

    context = {
        'login_form': login_form
    }

    return render(request, 'userauths/log-in.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('userauths:log-in'))
            else:
                # todo: show your account is activated message to user
                print('')

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'userauths/log-in.html', context)

    def post(self, request: HttpRequest):
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email_log')
            user_pass = login_form.cleaned_data.get('password_log')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email_log', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('core:index'))
                    else:
                        login_form.add_error('email_log', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email_log', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'userauths/log-in.html', context)


class ForgetPassword(View):
    def get(self, request):
        forget_password_form = UserForgetPasswordForm()
        context = {
            'forget_password_form': forget_password_form
        }
        return render(request, 'userauths/remember-password.html', context=context)

    def post(self, request: HttpRequest):
        forget_password_form = UserForgetPasswordForm(request.POST)
        if forget_password_form.is_valid():
            user_email = forget_password_form.cleaned_data.get('email_password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('فعال سازی حساب کاربری', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('core:index'))
        context = {
            'forget_password_form': forget_password_form
        }
        return render(request, 'userauths/remember-password.html', context=context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('userauths:log-in'))
        reset_password_form = UserResetPasswordForm()
        context = {
            'reset_password_form ': reset_password_form,
            'user': user
        }
        return render(request, 'userauths/reset-password.html', context=context)

    def post(self, request: HttpRequest, active_code):
        reset_password_form = UserResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_password_form.is_valid():
            if user is None:
                return redirect(reverse('userauths:log-in'))
            user_new_password = reset_password_form.cleaned_data.get('password1')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('userauths:log-in'))

        context = {
            'reset_password_form ': reset_password_form,
            'user': user
        }
        return render(request, 'userauths/reset-password.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('userauths:log-in'))
