from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import EditProfileModelForm

class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/profile.html'


class UserPanelInfo(View):
    def get(self, request: HttpRequest):
        edit_form = EditProfileModelForm
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel/profile-info.html', context=context)

    def post(self, request: HttpRequest):
        return render(request, 'user_panel/profile-info.html', {})


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/components/user_panel_menu_component.html')
