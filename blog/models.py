from django.db import models
from django.contrib.auth.models import User


class Publishable(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Publishable):
    title = models.CharField(max_length=128, blank=False, null=False)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(Publishable):
    content = models.TextField()
