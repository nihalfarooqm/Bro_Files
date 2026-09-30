from django.shortcuts import render
from .models import Post

# Create your views here.
# posts = [
#     {
#         'author': 'Nihal Farooq',
#         'title': 'First content',
#         'date_posted': '28/06/2026',
#         'content': 'The first'
#     },
#     {
#         'author': 'Lollipop',
#         'title': 'Second content',
#         'date_posted': '29/06/2026',
#         'content': 'The second'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all() #posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})