from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields=['username', 'email', 'phone', 'bio']

from django.contrib.auth import forms

def clean_email(self):

    email = self.cleaned_data['email']

    if CustomUser.objects.filter(email=email).exists():

        raise forms.ValidationError(
            'Email exists'
        )