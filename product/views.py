from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from .models import Product
from django.http import Http404


def product_detail(request, slug):
    # try:
    #     product_detail = Product.objects.get(pk=pk)
    # except:
    #     raise Http404
    product_detail = get_object_or_404(Product, slug=slug)
    context = {
        'product_detail': product_detail
    }
    return render(request, 'product/product_detail.html', context=context)


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data()
    #     slug = kwargs['slug']
    #     product_detail = get_object_or_404(Product, slug=slug)
    #     context['product'] = product_detail
    #     return context
    model = Product
