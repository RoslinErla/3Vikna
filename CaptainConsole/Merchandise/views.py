from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Merchandise').order_by('name')}
    return render(request, "merchandise/index.html", context)


def index2(request):
    context = {'products': Product.objects.filter(type='Merchandise').order_by('price')}
    return render(request, "merchandise/index.html", context)


def index3(request):
    context = {'products': Product.objects.filter(type='Merchandise').filter(manufacturer__icontains='Nintendo')}
    return render(request, 'merchandise/index.html', context)


def index4(request):
    context = {'products': Product.objects.filter(type='Merchandise').filter(manufacturer__icontains='Atari')}
    return render(request, 'merchandise/index.html', context)


def index5(request):
    context = {'products': Product.objects.filter(type='Merchandise').filter(manufacturer__icontains='sega')}
    return render(request, 'merchandise/index.html', context)


def index6(request):
    context = {'products': Product.objects.filter(type='Merchandise').filter(manufacturer__icontains='playstation')}
    return render(request, 'merchandise/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })
