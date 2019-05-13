from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
