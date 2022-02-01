from .models import Post
from django.views.generic import DetailView,ListView

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

