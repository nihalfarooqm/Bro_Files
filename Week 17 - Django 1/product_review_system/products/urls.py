from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('product/<int:id>/', views.ProductDetail.as_view(), name='detail'),
]