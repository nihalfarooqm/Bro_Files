from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('home/', views.home, name='home'),

]