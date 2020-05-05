from django.shortcuts import render

from AllProducts.models import Product

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Consoles').order_by('name')}
    return render(request, 'consoles/index.html', context)

