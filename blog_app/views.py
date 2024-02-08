# blog_app/views.py
from django.shortcuts import render, redirect
from blog_app.models import Post, Comment
from .forms import PostForm


# home.html
def home(request):
    posts = Post.objects.all()
    return render(request, "blog_app/home.html", {"posts": posts})


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, "blog_app/post.html", {"form": form})


def post_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    
    return render(request, "blog_app/post_category.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_app/post_detail.html", context)

