from django.http import HttpRequest
from django.shortcuts import render


def blog_view(request: HttpRequest):
    return render(request, 'blog/blog.html')


def posts(request: HttpRequest):
    return render(request, 'blog/all-posts.html')


def single_post(request: HttpRequest, slug):
    return render(request, 'blog/detail-post.html')
