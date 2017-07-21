from django.conf import settings
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True)
    photo = models.ImageField(blank=True)
    content = models.TextField()
    ip = models.GenericIPAddressField()

