from django.shortcuts import render
from .models import Post
from django.views import View

# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'posts/post_list.html', {
        'posts': posts
    })

class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)

        return render(request, 'posts/post_detail.html', {
            'post': post
        })