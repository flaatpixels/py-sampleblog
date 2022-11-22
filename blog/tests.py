from django.test import TestCase
from .models import Article
from .views import ArticlesListView
from django.urls import reverse

class ArticlesListViewTests(TestCase):

    def test_get_latest_articles(self):
        """
        get_latest_articles() returns all the specified number of articles
        in reverse chornological order
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles are available.")

        articles = []
        for i in range(50):
           article = Article(title = "article " + str(i + 1), content = "article content " + str(i + 1))
           article.save()
           articles.append(article)
        
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['articles'], reversed(articles[-15:]))