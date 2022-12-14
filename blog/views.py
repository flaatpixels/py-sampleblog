from .models import Article
from django.views.generic import ListView, DetailView, DeleteView

class ArticlesListView(ListView):
    paginate_by = 15
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-publish_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/show.html'
    context_object_name = 'article'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url ="/"
    template_name = "blog/confirm_delete.html"