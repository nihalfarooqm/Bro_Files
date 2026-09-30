from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

# Create your views here.

url = reverse('home')

# def home(request):
#     return HttpResponse("Welcome to the Home Page")

def home(request):
    # return HttpResponse("Welcome to the Home Page")
    # render(request, "home.html")
    # return render(request, "home.html", {
    #     "name": ["Nihal", 'Midlaj', 'Shafeer'],
    #     "age": [21, 22, 23],
    # })
    name = ["Nihal", 'Midlaj', 'Shafeer']
    age = [21, 24, 23]
    context = {
        'people': zip(name, age)
    }
    return render(request, "home.html", context)

# class HomeView(View):
#     def get(self, request):
        # return HttpResponse("Hello from Class-Based View")

class about(View):
    def get(self, request):
        return HttpResponse("About Page")
    
# def about(request):
#     return HttpResponse('About Page')