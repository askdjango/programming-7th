from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User


class Post(models.Model):
    # author = models.CharField(max_length=20)

    # user = models.ForeignKey(User)
    # user = models.ForeignKey("auth.User")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

