#blog_app/urls.py
from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<category>/", views.post_category, name="post_category"),
    path('registration/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]