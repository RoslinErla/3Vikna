from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product

# Create your views here.


def index(request):
    return render(request, 'cart/index.html')


def add_to_cart(request, id):
    #cart = user = (user=User.findbyid(request.user.id), product=product.findby(id))
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })
