from django.shortcuts import render

from AllProducts.models import Product

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Games').order_by('name')}
    return render(request, 'games/index.html', context)

def index2(request):
    context = {'products': Product.objects.filter(type='Games').order_by('price')}
    return render(request, 'games/index.html', context)