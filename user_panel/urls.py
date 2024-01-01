from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel'),
    path('profile-info/', views.UserPanelInfo.as_view(), name='profile_info'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password'),
]
