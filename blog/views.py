from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Blog, BlogCategory, BlogComment
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

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        blog: Blog = kwargs.get('object')
        context['comments'] = BlogComment.objects.filter(blog_id=blog.id, parent=None).order_by(
            '-create_date').prefetch_related(
            'blogcomment_set')
        return context



def add_blog_comment(request: HttpRequest):
    if request.user.is_authenticated:
        blog_id = request.GET.get('blog_id')
        blog_comment = request.GET.get('blog_comment')
        parent_id = request.GET.get('parent_id')
        print(blog_id, blog_comment, parent_id)
        new_comment = BlogComment(blog_id=blog_id, text=blog_comment, user_id=request.user.id, parent_id=parent_id)
        new_comment.save()

    return HttpResponse('response')
