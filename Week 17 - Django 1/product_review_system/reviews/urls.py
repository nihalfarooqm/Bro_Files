from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('profile/', views.profile, name='profile')
]