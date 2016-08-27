from django.test import TestCase
from django.contrib.auth.models import User

from ...models import Post


class PostTestCase(TestCase):
    def test_str(self):
        title = 'some title'
        user = User.objects.create()
        post = Post.objects.create(title=title, created_by=user)

        self.assertEqual(str(post), title)
