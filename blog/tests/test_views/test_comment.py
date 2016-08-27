from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ...models import Post


class CommentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_new = lambda x: reverse('blog:comment_new', args=(x,))
        self.user_name = 'temp'
        self.user_password = 'temp'
        self.user = User.objects.create_user(self.user_name, 'temp@gmail.com', self.user_password)
        self.other_user = User.objects.create_user('other', 'temp2@gmail.com', 'other')
        self.post = Post.objects.create(title='title', created_by=self.user)

    def test_create_has_logged_user(self):
        self.client.login(username=self.user_name, password=self.user_password)
        response = self.client.post(self.url_new(self.post.id), {'pk': self.post.id, 'content': 'content'})

        self.assertRedirects(response, reverse('blog:post_list'))
