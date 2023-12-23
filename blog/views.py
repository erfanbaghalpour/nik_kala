from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Blog, BlogCategory
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    # paginate_by = 4
    template_name = 'blog/blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        # context['date'] = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
        # paginator = Paginator(context['object_list'], 10)
        # page = self.request.GET.get('page')
        # try:
        #     paginated_objects = paginator.page(page)
        # except PageNotAnInteger:
        #     paginated_objects = paginator.page(1)
        # except EmptyPage:
        #     paginated_objects = paginator.page(paginator.num_pages)
        # context['paginated_objects'] = paginated_objects
        return context


def blog_categories_partial(request: HttpRequest):
    blog_main_categories = BlogCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        'main_categories': blog_main_categories
    }
    return render(request, 'blog', context=context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail-post.html'

    def get_queryset(self):
        query = super(BlogDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
