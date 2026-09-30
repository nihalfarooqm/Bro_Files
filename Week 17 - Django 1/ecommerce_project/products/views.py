from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()

    return render(request, 'products/home.html', {
        'products': products
    })


from django.views import View

class ProductDetailView(View):

    def get(self, request, id):
        product = Product.objects.get(id=id)

        return render(request, 'products/detail.html', {
            'product': product
        })
    
def New(request):
    return render(request, 'products/new.html')