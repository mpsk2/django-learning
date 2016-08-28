from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils import timezone

from ...models import Question


class IndexTestCase(TestCase):
    def test_simple(self):
        Question.objects.create(question_text='Q1', pub_date=timezone.now())
        Question.objects.create(question_text='Q2', pub_date=timezone.now())
        url = reverse('polls:index')
        client = Client()
        response = client.get(url)

        self.assertContains(response, 'Q1', status_code=200)
        self.assertContains(response, 'Q2', status_code=200)


class DetailTestCase(TestCase):
    def test_simple(self):
        Question.objects.create(question_text='Q1', pub_date=timezone.now())
        url = reverse('polls:detail', args=(1,))
        client = Client()
        response = client.get(url)

        self.assertContains(response, 'Q1', status_code=200)
