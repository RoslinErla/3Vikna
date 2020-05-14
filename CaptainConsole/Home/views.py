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

def add_to_cart(request, id):
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
        object = Cart.objects.filter(product_id=id, user_id=user).first()
        if object is not None:
            object.quantity += 1
            object.save()
            return redirect('cart-index')


        cart = Cart(product_id=id, user_id=user, quantity=1)
        cart.save()
        return redirect('cart-index')
    else:
        return redirect('login')




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