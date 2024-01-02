from django.urls import path
from . import views
from .views import IndexView, AboutView

app_name = 'core'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('/cat/<cat>', views.index, name='index-categories'),
#     path('about-us', views.AboutView.as_view(), name='about-us'),
#     # path('', views.HomeView.as_view(), name='index'),
# ]

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cat/<cat>', IndexView.as_view(), name='index-categories'),
    path('about-us', AboutView.as_view(), name='about-us'),
]
