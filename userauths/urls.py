from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    # path('sign-up', views.register_view, name='sign-up'),
    path('sign-up', views.RegisterView.as_view(), name='sign-up'),
    path('log-in', views.LoginView.as_view(), name='log-in'),
    path('log-out', views.LogoutView.as_view(), name='log-out'),
    path('forget-pass', views.ForgetPassword.as_view(), name='forget-pass'),
    path('reset-pass/<active_code>', views.ResetPasswordView.as_view(), name='reset-pass'),
    # path('log-in', views.login_view, name='log-in'),
    path('activate-account/<str:email_active_code>', views.ActivateAccountView.as_view(), name='activate-account'),
]
