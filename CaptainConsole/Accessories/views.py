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
    context = {'products': Product.objects.filter(type='Accessories').order_by('name')}
    return render(request, "accessories/index.html", context)


def index2(request):
    context = {'products': Product.objects.filter(type='Accessories').order_by('price')}
    return render(request, "accessories/index.html", context)


def index3(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='Nintendo')}
    return render(request, 'accessories/nintendo.html', context)


def index4(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='Atari')}
    return render(request, 'accessories/atari.html', context)


def index5(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='sega')}
    return render(request, 'accessories/sega.html', context)


def index6(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='playstation')}
    return render(request, 'accessories/playstation.html', context)


def index7(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='Atari').order_by('price')}
    return render(request, 'accessories/atari.html', context)


def index8(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='Nintendo').order_by('price')}
    return render(request, 'accessories/nintendo.html', context)


def index9(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='playstation').order_by('price')}
    return render(request, 'accessories/playstation.html', context)


def index10(request):
    context = {'products': Product.objects.filter(type='Accessories').filter(manufacturer__icontains='sega').order_by('price')}
    return render(request, 'accessories/sega.html', context)


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
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id )

    })

