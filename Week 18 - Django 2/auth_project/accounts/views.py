from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):

    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')
    
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):

    logout(request)

    return redirect('login')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from .forms import ContactForm

def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    
    else:

        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

## custom validation example
# def clean_name(self):

#     name = self.cleaned_data['name']

#     if len(name) < 3:
#         raise forms.ValidationError(
#             "Name too short"
#         )
    
#     return name

from .forms import PostForm

def post_view(request):

    if request.method == 'POST':
        post = PostForm(request.POST)

        if post.is_valid():
            post.save()

    else:
        post = PostForm()

    return redirect('dashboard')