from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.db.models import Avg
from django.views.generic.base import TemplateView
from django.views import View
from django.core.paginator import Paginator

from site_module.models import SiteSetting, Slider


def index(request):
    products = Product.objects.all().order_by('-title')
    number_of_products = products.count()
    # avg_rating = products.aggregate(Avg('rating'))
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    products_list = paginator.get_page(page_number)
    sliders = Slider.objects.filter(is_active=True)
    context = {
        'products': products_list,
        'total_number_of_products': number_of_products,
        'sliders': sliders
        # 'average_ratings': avg_rating,
    }
    return render(request, 'core/index.html', context=context)


# class HomeView(View):
#     def get(self, request):
#         products = Product.objects.all().order_by('-title')
#         context = {
#             'product': products
#         }
#         return render(request, 'core/index.html', context=context)
# class HomeView(TemplateView):
#     template_name = 'core/index.html'


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'partials/site_header_component.html', context=context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'partials/site_footer_component.html', context=context)


class AboutView(TemplateView):
    template_name = 'core/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting

        return context

