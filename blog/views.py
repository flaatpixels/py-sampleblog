from django.http import HttpResponse
from .models import Article
from django.template import loader

def index(request):
    latest_articles_list = Article.objects.all()
    template = loader.get_template('blog/index.html')
    return HttpResponse(template.render({'latest_articles_list': latest_articles_list}, request))

def show(request, article_id):
    article = Article.objects.get(pk=article_id)
    template = loader.get_template('blog/show.html')
    return HttpResponse(template.render({'article': article}, request))