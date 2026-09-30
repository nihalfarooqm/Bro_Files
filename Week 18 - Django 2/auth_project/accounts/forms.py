from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    message = forms.CharField(widget=forms.Textarea)

    # me = forms.Textarea() ## test

from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):

    class Meta:
        
        model = Post

        fields = ['title', 'content']