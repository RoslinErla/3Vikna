from django.contrib.auth.forms import UserCreationForm  ## Ekki viss um user creation form vegna þess að er að búa til admin
from django.shortcuts import render

# new admin login credentials

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=requestPOST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'admin/register.html', {
            'form': UserCreationForm()
        })