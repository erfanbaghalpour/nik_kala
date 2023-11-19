from django.shortcuts import render, get_object_or_404
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
