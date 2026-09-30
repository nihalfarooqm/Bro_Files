# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello World! From Home')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('From About')
    return render(request, 'about.html')