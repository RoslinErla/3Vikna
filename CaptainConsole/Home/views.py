from django.shortcuts import render
from AllProducts.models import Product
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {'products': Product.objects.filter(recommended=True).order_by('name')}
    return render(request, "home/index.html", context)

