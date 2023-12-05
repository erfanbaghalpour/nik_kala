from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    # path('sign-up', views.register_view, name='sign-up'),
    path('sign-up', views.RegisterView.as_view(), name='sign-up'),
    path('log-in', views.LoginView.as_view(), name='log-in'),
]
