from django.urls import path, include
from . import views
# from blog.views import home, HomeView

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about.as_view()),
]