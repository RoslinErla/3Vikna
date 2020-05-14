from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from AllProducts.models import Product

# Create your views here.
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
    context = {'products': Product.objects.filter(type='Games').order_by('name')}
    return render(request, 'games/index.html', context)


def index2(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').order_by('price')}
    return render(request, 'games/index.html', context)


def index3(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Nintendo')}
    return render(request, 'games/nintendo.html', context)


def index4(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Atari')}
    return render(request, 'games/atari.html', context)


def index5(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='sega')}
    return render(request, 'games/sega.html', context)


def index6(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='playstation')}
    return render(request, 'games/playstation.html', context)


def index7(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Atari').order_by('price')}
    return render(request, 'games/atari.html', context)


def index8(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Nintendo').order_by('price')}
    return render(request, 'games/nintendo.html', context)


def index9(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='playstation').order_by('price')}
    return render(request, 'games/playstation.html', context)


def index10(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='sega').order_by('price')}
    return render(request, 'games/sega.html', context)


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
        already_there = Search.objects.filter(product_id=id, user_id=user).first()
        if not already_there:
            search = Search(product_id=id, user_id=user)
            search.save()
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })
