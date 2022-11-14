from .models import Article
from django.views.generic import ListView, DetailView

class ArticlesListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/show.html'
    context_object_name = 'article'