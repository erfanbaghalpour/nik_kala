from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.db.models import Avg
from django.views.generic.base import TemplateView
from django.views import View


def index(request):
    products = Product.objects.all().order_by('-title')
    number_of_products = products.count()
    # avg_rating = products.aggregate(Avg('rating'))
    context = {
        'products': products,
        'total_number_of_products': number_of_products,
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
    return render(request, 'partials/site_header_component.html', {})


def site_footer_component(request):
    return render(request, 'partials/site_footer_component.html', {})
