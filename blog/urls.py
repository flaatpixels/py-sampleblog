from django.urls import path
from blog.views import ArticlesListView, ArticleDetailView

from . import views

urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='show'),
]