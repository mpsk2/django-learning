from django.db import models
from django.contrib.auth.models import User


class Publishable(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        abstract = True

    def short_content(self):
        if not self.content:
            return self.content
        elif len(self.content) < 15:
            return self.content
        else:
            return self.content[:15] + '...'


class Post(Publishable):
    title = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.title


class Comment(Publishable):
    post = models.ForeignKey(Post)
