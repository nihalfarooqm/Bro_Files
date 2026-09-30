from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create'),
    path('update/<int:id>/', views.update_task, name='update'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('task/<int:id>/', views.TaskDetailView.as_view(), name='detail'),
    path('api/tasks/', views.TaskListAPI.as_view(), name='api_tasks')
]