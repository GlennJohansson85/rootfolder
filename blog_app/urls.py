# ======================================
#                       BLOG_APP/URLS.PY
# ======================================
from django.urls import path
from blog_app import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path("category/<category>/", views.post_category, name="post_category"),
    path('registration/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
