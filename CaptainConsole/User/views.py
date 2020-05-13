from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

from User.models import Profile
from django.shortcuts import render, redirect, get_object_or_404

from User.forms.profile_form import ProfileForm
from User.forms.forms import NewUserForm
from User.models import Profile
from Search.models import Search
from AllProducts.models import Product


def register(request):
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            image = Profile(user_id=user.id)
            image.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'admin/register.html', {
         'form': form
        })


def profile(request):
    if 'search_filter' in request.GET:
        search = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search)]
        return JsonResponse({'data': products})
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    return render(request, 'admin/profile.html', {
        'form': ProfileForm(instance=profile)
    })

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

    return render(request, 'home/product_details.html', {
        'products': get_object_or_404(Product, pk=id)
    })


def browsing_history(request):
    user = request.user.id
    context = {'products': Search.objects.filter(user_id=user)}
    context_list = list()
    for objects in context['products']:
        context_list.append(Product.objects.filter(id=objects.product_id).first())
    context = {'products': context_list}
    return render(request, 'admin/history.html', context)


