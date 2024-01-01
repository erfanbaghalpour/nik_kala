from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from userauths.models import User
from .forms import EditProfileModelForm


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/profile.html'


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


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/components/user_panel_menu_component.html')
