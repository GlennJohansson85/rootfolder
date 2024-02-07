# blog_app/views.py
from django.shortcuts import render
from blog_app.models import Post, Comment


# Model for Main page
def home(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    
    return render(request, "blog_app/home.html", context)


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

