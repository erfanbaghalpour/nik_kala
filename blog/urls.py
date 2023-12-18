from django.urls import path
from . import views

#
# urlpatterns = [
#     path('', views.blog_view, name="index_blog"),
#     path('all-posts', views.posts, name="post_blog"),
#     path('detail/<slug:slug>', views.single_post, name="single_post")
#     # path('detail/', views.single_post, name="single_post")
# ]


urlpatterns = [
    # path('', views.blog_view, name="index_blog"),
    path('all-posts/', views.posts, name="post_blog"),
    path('detail/<slug:slug>/', views.single_post, name="single_post"),
    path('', views.BlogListView.as_view(), name="index_blog"),
]
