from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination
from .pagination import PostPagination

# Create your views here.
@login_required
def create_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)

            post.author = request.user

            post.save()

            return redirect('posts:list')
        
    else:
        form = PostForm()

    return render(request, "posts/create.html", {
        "form": form
    })

def post_list(request):
    posts = Post.objects.all()

    return render(request, "posts/list.html", {
        "posts": posts
    })

class PostDetailView(View):

    def get(self, request, id):
        post = Post.objects.get(id=id)

        return render(request, "posts/detail.html", {
            "post": post
        })
    
class PostAPI(APIView):

    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    def get(self, request):
        posts = Post.objects.all()

        paginator = PostPagination()
        paginated_posts = paginator.paginate_queryset(posts, request)

        serializer = PostSerializer(paginated_posts, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)
    
@login_required
def update_post(request, id):

    post = Post.objects.get(id=id)

    if post.author != request.user:
        return redirect('posts:list')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:detail', id=post.id)

    else:
        form = PostForm(instance=post)

    return render(request, "posts/update.html", {
        "form": form
    })

@login_required
def delete_post(request, id):

    post = Post.objects.get(id=id)

    if post.author == request.user:
        post.delete()

    return redirect('posts:list')

class PostDetailAPI(APIView):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"message": "Deleted"})