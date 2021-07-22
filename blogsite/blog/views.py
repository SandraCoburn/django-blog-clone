from django.shortcuts import render
from django.utils import timezone
from django.views.generic import (TemplateView, ListView)
from blog.models import Post, Comment

# Create your views here.
class AboutView(TemplateView):
  template_name = 'about.html'

class PostListView(ListView):
  model = Post

  #like a sql query on the model. lte -> less than or equal to. Order by more recent date
  def get_queryset(self):
    return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

