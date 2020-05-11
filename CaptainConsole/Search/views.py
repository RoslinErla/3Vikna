from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from AllProducts.models import Product
from Search.models import Search


# Create your views here.

def browse_history(request, user_id):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    return render(request, 'allProducts/index.html', {
        'products': get_object_or_404(Search, user_id=id)
    })