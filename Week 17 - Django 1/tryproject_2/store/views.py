from django.shortcuts import render
from .models import Products

# Create your views here.

def product_list(request):
    print('view called')
    items = Products.objects.all()

    return render(request, 'product_list.html', {
        'products' : items
    })