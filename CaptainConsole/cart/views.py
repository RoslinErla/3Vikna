from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from AllProducts.models import Product
from cart.models import Cart

# Create your views here.
from cart.forms.checkout_form import CheckoutForm
from cart.models import Checkout


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


def cart(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    context = {'products': Cart.objects.filter(user_id=request.user.id)}
    total_price = 0
    product_list = []
    for o in context['products']:
        product_list.append((Product.objects.filter(id=o.product_id).first(), o.quantity))
        total_price += Product.objects.filter(id=o.product_id).first().price * o.quantity
    context = {'products': product_list, 'total': total_price}
    print(context)
    return render(request, 'cart/cart-index.html', context)


def remove_product(request, id):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})

    user = request.user.id
    object = Cart.objects.filter(product_id=id, user_id=user).first()

    if object.quantity == 1:
        object.delete()
    else:
        object.quantity -= 1
        object.save()
    return redirect('cart-index')


def checkout(request):
    user = request.user.id
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            checkout = Checkout(Full_name=request.POST['Full_name'], Address=request.POST['Address'], City=request.POST['City'],
                                Postal_code=request.POST['Postal_code'], Name_of_cardholder=request.POST['Name_of_cardholder'],
                                Card_number=request.POST['Card_number'], Expiration_date=request.POST['Expiration_date'],
                                CVC=request.POST['CVC'], User_id=user)
            checkout.save()
            return redirect('read-only')
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {
        'form': form
    })


def read_only_review(request):
    user = request.user.id
    context2 = {'products': Cart.objects.filter(user_id=user)}
    product_list = list()
    for elements in context2['products']:
        product_list.append(Product.objects.filter(id=elements.product_id).first())

    context = {'information': Checkout.objects.filter(User_id=user), 'products': product_list}

    return render(request, 'cart/read_only.html', context)


def success(request):
    user = request.user.id
    checkout = get_object_or_404(Checkout, User_id=user)
    cart = get_object_or_404(Cart, user_id=user)
    cart.delete()
    checkout.delete()
    return render(request, 'cart/Success.html')

