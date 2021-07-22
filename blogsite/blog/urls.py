from django.utils.timezone import now
from blogsite.blog.views import PostListView
from django.urls import path
from blog import views

urlpatterns = [
  path('', views.PostListView.as_view(), name='post_list'),
  path('about/', views.AboutView.as_view(), name='about'),
]