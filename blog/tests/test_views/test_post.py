from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ...models import Post


class PostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_new = reverse('blog:post_new')
        self.url_delete = lambda x: reverse('blog:post_delete', args=(x.id,))
        self.url_edit = lambda x: reverse('blog:post_edit', args=(x.id,))
        self.user_name = 'temp'
        self.user_password = 'temp'
        self.user = User.objects.create_user(self.user_name, 'temp@gmail.com', self.user_password)
        self.other_user = User.objects.create_user('other', 'temp2@gmail.com', 'other')

    def test_create_not_logged_in(self):
        response = self.client.get(self.url_new)
        self.assertRedirects(response, reverse('account_login') + '?next=' + self.url_new, status_code=302,
                             target_status_code=200)

    def test_create_logged_in_do_not_redirect(self):
        self.client.login(username=self.user_name, password=self.user_password)
        response = self.client.get(self.url_new)
        self.assertEqual(response.status_code, 200)

    def test_create_has_logged_user(self):
        self.client.login(username=self.user_name, password=self.user_password)
        response = self.client.post(self.url_new, {'title': 'title', 'content': 'content'})

        self.assertRedirects(response, reverse('blog:post_list'), status_code=302, target_status_code=200)

        post = Post.objects.last()

        self.assertEqual(post.created_by, self.user)
        self.assertEqual(post.title, 'title')
        self.assertEqual(post.content, 'content')

    def test_delete_post_fail_not_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)

        response = self.client.post(self.url_delete(post))
        self.assertEqual(response.status_code, 403)

    def test_delete_get_fail_not_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)

        response = self.client.get(self.url_delete(post))
        self.assertEqual(response.status_code, 403)

    def test_update_post_fail_not_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)

        response = self.client.post(self.url_edit(post))
        self.assertEqual(response.status_code, 403)

    def test_update_get_fail_not_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)

        response = self.client.get(self.url_edit(post))
        self.assertEqual(response.status_code, 403)

    def test_delete_post_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.post(self.url_delete(post))
        self.assertRedirects(response, reverse('blog:post_list'), status_code=302, target_status_code=200)

    def test_delete_get_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.get(self.url_delete(post))
        self.assertEqual(response.status_code, 200)

    def test_update_post_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.post(self.url_edit(post))
        self.assertEqual(response.status_code, 200)

    def test_update_get_logged(self):
        post = Post.objects.create(title='abc', created_by=self.user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.get(self.url_edit(post))
        self.assertEqual(response.status_code, 200)

    def test_delete_post_fail_other_logged(self):
        post = Post.objects.create(title='abc', created_by=self.other_user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.post(self.url_delete(post))
        self.assertEqual(response.status_code, 403)

    def test_delete_get_fail_other_logged(self):
        post = Post.objects.create(title='abc', created_by=self.other_user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.get(self.url_delete(post))
        self.assertEqual(response.status_code, 403)

    def test_update_post_fail_other_logged(self):
        post = Post.objects.create(title='abc', created_by=self.other_user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.post(self.url_edit(post))
        self.assertEqual(response.status_code, 403)

    def test_update_get_fail_other_logged(self):
        post = Post.objects.create(title='abc', created_by=self.other_user)
        self.client.login(username=self.user_name, password=self.user_password)

        response = self.client.get(self.url_edit(post))
        self.assertEqual(response.status_code, 403)
