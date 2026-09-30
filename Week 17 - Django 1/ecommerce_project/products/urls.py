from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/<int:id>/', views.ProductDetailView.as_view(), name='detail'),
    path('new/', views.New, name = 'new'),
]