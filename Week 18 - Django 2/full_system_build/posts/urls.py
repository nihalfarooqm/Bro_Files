from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.create_post, name='create'),
    path('<int:id>/', views.PostDetailView.as_view(), name='detail'),
    path('api/posts/', views.PostAPI.as_view(), name='api_posts'),
    path('<int:id>/update/', views.update_post, name='update'),
    path('<int:id>/delete/', views.delete_post, name='delete'),
    path('api/posts/', views.PostAPI.as_view()),
    path('api/posts/<int:id>/', views.PostDetailAPI.as_view()),
]