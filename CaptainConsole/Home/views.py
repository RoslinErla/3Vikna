from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {'products': Product.objects.filter(recommended=True).order_by('name')}
    return render(request, "home/index.html", context)


# /home/1
def get_product_by_id(request, id):
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id )

    })