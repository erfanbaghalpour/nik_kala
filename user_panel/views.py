from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import logout
from userauths.models import User
from .forms import EditProfileModelForm, ChangePasswordForm
from django.urls import reverse


# class UserPanelDashboardPage(TemplateView):
#     template_name = 'user_panel/profile.html'
class UserPanelDashboardPage(View):
    def get(self, request: HttpRequest):
        profile = User.objects.filter(id=request.user.id).first()
        context = {
            'profile': profile
        }
        return render(request, 'user_panel/profile.html', context=context)


class UserPanelInfo(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'user': current_user,
        }
        return render(request, 'user_panel/profile-info.html', context=context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form,
            'user': current_user,

        }
        return render(request, 'user_panel/profile-info.html', context=context)


class ChangePassword(View):
    def get(self, request: HttpRequest):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel/change-password.html', context=context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('userauths:log-in'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')

        context = {
            'form': form
        }
        return render(request, 'user_panel/change-password.html', context=context)


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/components/user_panel_menu_component.html')
