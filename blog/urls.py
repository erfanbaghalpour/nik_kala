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
    # path('detail/<slug:slug>/', views.single_post, name="single_post"),
    path('', views.BlogListView.as_view(), name="index_blog"),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name="single_blog"),
    path('add-blog-comment', views.add_blog_comment, name='add_blog_comment')

]
