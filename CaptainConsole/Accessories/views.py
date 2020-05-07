from django.shortcuts import render

from AllProducts.models import Product

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Accessories').order_by('name')}
    return render(request, "accessories/index.html", context)


def index2(request):
    context = {'products': Product.objects.filter(type='Accessories').order_by('price')}
    return render(request, "accessories/index.html", context)