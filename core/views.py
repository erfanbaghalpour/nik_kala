from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'core/index.html', context=context)


