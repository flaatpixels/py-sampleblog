from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-publish_at']
    readonly_fields = ['publish_at']
    exclude = ['slug']

admin.site.register(Article, ArticleAdmin)

# Register your models here.
