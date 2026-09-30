from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def register(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('accounts:login')
    
    return render(request, "accounts/register.html")

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:list')
        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid credentials"
            })
        
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect('accounts:login')