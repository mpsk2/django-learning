from django.test import TestCase

from ...models import Publishable


class PublishableTestCase(TestCase):
    def test_content_empty(self):
        publishable = Publishable(content='')
        self.assertEqual(publishable.short_content(), '')

        publishable = Publishable(content=None)
        self.assertEqual(publishable.short_content(), None)

    def test_content_too_short(self):
        publishable = Publishable(content='abc')
        self.assertEqual(publishable.short_content(), 'abc')

    def test_content_too_long(self):
        publishable = Publishable(content='too long, too long, too long, too long, too long')
        self.assertEqual(publishable.short_content(), 'too long, too l...')
