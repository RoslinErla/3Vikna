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
    # cart = user = (user=User.findbyid(request.user.id), product=product.findby(id))
    if request.user.is_authenticated:
        user = request.user.id
        cart = Cart(product_id=id, user_id=user)
        cart.save()
        return redirect('cart-index')
    else:
        return redirect('login')


def cart(request):
    context = {'products': Cart.objects.filter(user_id=request.user.id)}
    return render(request, 'cart/cart-index.html', context)


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
    context = {'information': Checkout.objects.filter(User_id=user)}
    return render(request, 'cart/read_only.html', context)
