from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product

# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    return render(request, 'cart/index.html')


def add_to_cart(request, id):
    #cart = user = (user=User.findbyid(request.user.id), product=product.findby(id))
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })
