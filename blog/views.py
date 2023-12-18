from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import Blog
from django.views.generic.list import ListView


def blog_view(request: HttpRequest):
    return render(request, 'blog/blog.html')


def posts(request: HttpRequest):
    return render(request, 'blog/all-posts.html')


def single_post(request: HttpRequest, slug):
    return render(request, 'blog/detail-post.html')


class BlogView(View):
    def get(self, request):
        blog = Blog.objects.filter(is_active=True)
        context = {
            'blog': blog
        }
        return render(request, 'blog/blog.html', context=context)


class BlogListView(ListView):
    model = Blog
    paginate_by = 4
    template_name = 'blog/blog.html'
