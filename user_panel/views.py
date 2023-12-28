from django.shortcuts import render
from django.views.generic import TemplateView


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/profile.html'
