from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product
from django.http import HttpResponse, JsonResponse
from Search.models import Search


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
    context = {'products': Product.objects.filter(recommended=True).order_by('name')}
    return render(request, "home/index.html", context)


def get_product_by_id(request, id):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    if request.user.is_authenticated:
        user = request.user.id
        search = Search(product_id=id, user_id=user)
        search.save()
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id )

    })