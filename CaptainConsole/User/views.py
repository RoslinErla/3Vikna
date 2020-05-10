from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# new admin login credentials


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
    pass


