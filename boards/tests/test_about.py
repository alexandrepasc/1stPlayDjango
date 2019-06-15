from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board


class TestUrls(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        Board.objects.create(name='Python', description='Python board.')

    def test_about_topic_connection(self):
        path = reverse('about')
        response = self.client.get(path)
        # self.assertContains(self.response, 'href="/"'.format('about/'))
        self.assertNotContains(response, 'href="/board/1"'.format('about/'))