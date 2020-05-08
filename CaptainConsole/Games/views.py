from django.shortcuts import render

from AllProducts.models import Product

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Games').order_by('name')}
    return render(request, 'games/index.html', context)


def index2(request):
    context = {'products': Product.objects.filter(type='Games').order_by('price')}
    return render(request, 'games/index.html', context)


def index3(request):
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Nintendo')}
    return render(request, 'games/index.html', context)


def index4(request):
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='Atari')}
    return render(request, 'games/index.html', context)


def index5(request):
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='sega')}
    return render(request, 'games/index.html', context)


def index6(request):
    context = {'products': Product.objects.filter(type='Games').filter(manufacturer__icontains='playstation')}
    return render(request, 'games/index.html', context)
