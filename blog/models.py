from django.db import models
from mdeditor.fields import MDTextField
from django.template.defaultfilters import slugify

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()
    publish_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length= 250, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)