from django.shortcuts import render
from .models import Task

from .forms import TaskForm
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

from django.views import View

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):

    tasks = Task.objects.filter(user=request.user)

    return render(request, "tasks/home.html", {
        "tasks": tasks
    })

# def create(request):
#     return render(request, "tasks/create.html")

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:home')
    else:
        form = TaskForm()

    return render(request, "tasks/create.html", {
        "form": form
    })

def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if task.user != request.user:
        return redirect('tasks:home')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks:home')
        
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/update.html", {
        "form": form
    })

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if task.user == request.user:
        task.delete()

    return redirect('tasks:home')

class TaskDetailView(LoginRequiredMixin, View):
    def get(self, request, id):

        task = get_object_or_404(
            Task,
            id=id,
            user=request.user
        )

        return render(request, "tasks/detail.html", {
            "task": task
        })
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

class TaskListAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):

        tasks = Task.objects.filter(user=request.user)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)
    
    def post(self, request):

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['completed']

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        )
    
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )