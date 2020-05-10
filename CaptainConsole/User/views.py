from django.contrib.auth.forms import UserCreationForm
from User.models import Profile
from django.shortcuts import render, redirect

from User.forms.profile_form import ProfileForm
from User.models import Profile


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'admin/register.html', {
         'form': form
        })


def profile(request):
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


