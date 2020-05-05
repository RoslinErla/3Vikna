from django.shortcuts import render
from AllProducts.models import Product

# Create your views here.


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'allProducts/index.html', context)

