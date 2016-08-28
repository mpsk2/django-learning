from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexTestCase(TestCase):
    def test_simple(self):
        url = reverse('polls:index')
        client = Client()
        response = client.get(url)

        self.assertContains(response, "Hello, world. You're at the polls index.", status_code=200)
