from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from AllProducts.models import Product, ProductImage
from AllProducts.forms.product_form import ProductCreateForm, ProductUpdateForm


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
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'allProducts/index.html', context)


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
    context = {'products': Product.objects.all().order_by('price')}
    return render(request, 'allProducts/index.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains="Nintendo").order_by('name')}
    return render(request, 'allProducts/nintendo.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains="Atari").order_by('name')}
    return render(request, 'allProducts/atari.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains="Sega").order_by('name')}
    return render(request, 'allProducts/sega.html', context)


def index6(request):
    context = {'products': Product.objects.filter(manufacturer__icontains="Playstation").order_by('name')}
    return render(request, 'allProducts/playstation.html', context)

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
    context = {'products': Product.objects.filter(manufacturer__icontains='Atari').order_by('price')}
    return render(request, 'allProducts/atari.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains='Nintendo').order_by('price')}
    return render(request, 'allProducts/nintendo.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains='playstation').order_by('price')}
    return render(request, 'allProducts/playstation.html', context)


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
    context = {'products': Product.objects.filter(manufacturer__icontains='sega').order_by('price')}
    return render(request, 'allProducts/sega.html', context)


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
        already_there = Search.objects.filter(product_id=id)
        if not already_there:
            search = Search(product_id=id, user_id=user)
            search.save()
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })


def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            image = ProductImage(image=request.POST['image'], Product_id=product.id)
            image.save()
            return redirect('home-index')
    else:
        form = ProductCreateForm()

    return render(request, 'allProducts/create_product.html', {
        'form': form
    })


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('home-index')


def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('allProduct_details', id=id)

    else:
        form = ProductUpdateForm(instance=instance)

    return render(request, 'allProducts/update_product.html', {
        'form': form,
        'id': id
    })
