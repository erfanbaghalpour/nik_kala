from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    # path('sign-up', views.register_view, name='sign-up'),
    path('sign-up', views.RegisterView.as_view(), name='sign-up'),
    path('log-in', views.LoginView.as_view(), name='log-in'),
    # path('log-in', views.login_view, name='log-in'),
    path('activate-account/<str:email_active_code>', views.ActivateAccountView.as_view(), name='activate-account'),
]
