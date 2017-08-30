from django.shortcuts import render,redirect
from .models import Post

from .forms_new_post import PostsForm


def home(request):

    all_posts=Post.objects.all()

    context={
        'all_posts':all_posts
    }
    return render(request,'index.html',context)



def post_list(request):

    all_posts=Post.objects.all().order_by('-id')

    context={
        'all_posts':all_posts
    }
    return render(request,'all_post.html',context)


def single_post(request,post_id):
    post = Post.objects.get(id=post_id)
    print(post)
    context={
        'post':post
    }
    return render(request,'single_post.html',context)

def add_posts(request):

    if request.method == 'POST':
        form=PostsForm(request.POST)
        form.save()
        return redirect('post_lists')
    else:
        form=PostsForm

    return render(request,'add_new_post.html',{'form':form})

