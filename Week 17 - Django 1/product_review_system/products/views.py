from django.shortcuts import render
from .models import Product
from django.views import View

# Create your views here.
def product_list(request):
    products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products
    })

class ProductDetail(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)

        return render(request, 'products/product_detail.html', {
            'product': product
        })