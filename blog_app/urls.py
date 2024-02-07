#blog_app/urls.py
from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<category>/", views.post_category, name="post_category"),
]