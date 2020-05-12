from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from AllProducts.models import Product

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
    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })


def checkout(request):
    User = request.user.id
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            checkout = Checkout(Full_name=request.POST['Full_name'], Address=request.POST['Address'], City=request.POST['City'],
                                Postal_code=request.POST['Postal_code'], Name_of_cardholder=request.POST['Name_of_cardholder'],
                                Card_number=request.POST['Card_number'], Expiration_date=request.POST['Expiration_date'],
                                CVC=request.POST['CVC'], User_id=User)
            checkout.save()
            return redirect('home-index')
    else:
        form = CheckoutForm()

    return render(request, 'cart/checkout.html', {
        'form': form
    })
