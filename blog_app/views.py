# blog_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from blog_app.models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse
import logging



def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'blog_app/user_registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'blog_app/user_login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


# home.html
@login_required
def home(request):
    # Order posts by 'created_on' in descending order
    posts = Post.objects.all().order_by('-created_on')
    return render(request, "blog_app/home.html", {"posts": posts})


def post_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    
    return render(request, "blog_app/post_category.html", context)


@login_required  
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, "blog_app/post.html", {"form": form})

print("Comment view called!")
logger = logging.getLogger(__name__)

@login_required
def comment(request, post_id):
    print(request.POST)
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                comment = form.save(commit=False)
                comment.author = request.user
                comment.save()

                # Redirect to the home page - anchor post
                return redirect(reverse('home') + f'#{post_id}')
            except Exception as e:
                logger.error(f"Error saving comment: {e}")
                # Log the form data for debugging
                logger.error(f"Form data: {request.POST}")
        else:
            logger.error(f"Invalid form: {form.errors}")
            # Log the form data for debugging
            logger.error(f"Form data: {request.POST}")
    else:
        form = CommentForm()

    return render(request, 'blog_app/home.html', {'post': post, 'form': form})