from django.shortcuts import render
from AllProducts.models import Product
from django.http import HttpResponse


# Create your views here.

def index(request):
<<<<<<< HEAD
    context = {'products': Product.objects.filter(type="consoles").order_by('name')}
    return render(request, "home/index.html", context)
=======
    return render(request, "home/index.html")

>>>>>>> 19811e4d5a7f7da1861d2874e13fef7ce91dd078
