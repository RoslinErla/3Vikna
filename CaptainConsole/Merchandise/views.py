from django.shortcuts import render
from AllProducts.models import Product
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'products': Product.objects.filter(type='Merchandise').order_by('name')}
    return render(request, "merchandise/index.html", context)


def index2(request):
    context = {'products': Product.objects.filter(type='Merchandise').order_by('price')}
    return render(request, "merchandise/index.html", context)