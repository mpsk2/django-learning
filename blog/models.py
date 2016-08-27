from django.db import models
from django.contrib.auth.models import User


class Publishable(models.Model):
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Publishable):
    title = models.CharField(max_length=128, blank=False, null=False)
    content = models.TextField()


class Comment(Publishable):
    content = models.TextField()
