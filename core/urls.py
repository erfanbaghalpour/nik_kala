from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.AboutView.as_view(), name='about-us'),
    # path('', views.HomeView.as_view(), name='index'),
]
