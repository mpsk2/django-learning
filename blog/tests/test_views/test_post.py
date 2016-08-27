from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_new = reverse('blog:post_new')
        self.user_name = 'temp'
        self.user_password = 'temp'
        self.user = User.objects.create_user(self.user_name, 'temp@gmail.com', self.user_password)

    def test_post_create_not_logged_in(self):
        response = self.client.get(self.url_new)
        self.assertRedirects(response, reverse('account_login') + '?next=' + self.url_new, status_code=302,
                             target_status_code=200)

    def test_post_create_logged_in_do_not_redirect(self):
        self.client.login(username=self.user_name, password=self.user_password)
        response = self.client.get(self.url_new)
        self.assertEqual(response.status_code, 200)



