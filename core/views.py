from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product
from django.db.models import Avg

def index(request):
    products = Product.objects.all().order_by('-title')
    number_of_products = products.count()
    avg_rating = products.aggregate(Avg('rating'))
    context = {
        'products': products,
        'total_number_of_products': number_of_products,
        'average_ratings': avg_rating,
    }
    return render(request, 'core/index.html', context=context)


