from django.shortcuts import render

from AllProducts.models import Product

# Create your views here.


def index(request):
    return render(request, 'cart/index.html')
