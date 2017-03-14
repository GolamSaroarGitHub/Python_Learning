from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):

    all_post=Post.objects.all()
    return render(request, 'index.html',{'all_post_list': all_post})

def show_all_posts(request):
    all_posts=Post.objects.all()
    return render(request,'post_list.html',{'all_post_list': all_posts})


def single_post(request,post_id):
    post=Post.objects.get(pk=post_id)
    print(post)

    return render(request,'single_post.html',{'post':post})