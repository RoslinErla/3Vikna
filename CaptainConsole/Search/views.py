from django.shortcuts import render, get_object_or_404
from Search.models import Search


# Create your views here.

def browse_history(request, user_id):
    return render(request, 'allProducts/index.html', {
        'products': get_object_or_404(Search, user_id=id)
    })