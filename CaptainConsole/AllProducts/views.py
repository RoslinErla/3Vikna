from django.shortcuts import render, get_object_or_404
from AllProducts.models import Product


# Create your views here.


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'allProducts/index.html', context)


def index2(request):
    context = {'products': Product.objects.all().order_by('price')}
    return render(request, 'allProducts/index.html', context)


def index3(request):
    context = {'products': Product.objects.filter(manufacturer__icontains="Nintendo")}
    return render(request, 'allProducts/index.html', context)


def index4(request):
    context = {'products': Product.objects.filter(manufacturer__icontains="Atari")}
    return render(request, 'allProducts/index.html', context)


def index5(request):
    context = {'products': Product.objects.filter(manufacturer__icontains="Sega")}
    return render(request, 'allProducts/index.html', context)


def index6(request):
    context = {'products': Product.objects.filter(manufacturer__icontains="Playstation")}
    return render(request, 'allProducts/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })


def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ProductCreateForm()

    return render(request, 'allProducts/create_product.html', {
        'form': form
    })