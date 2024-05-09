from django.shortcuts import render
from catalog.models import Product

def product_list(request):
    product_list = Product.objects.all()

    context = {
        'product_list' : product_list
    }
    return render(request, 'product_list.html', context)