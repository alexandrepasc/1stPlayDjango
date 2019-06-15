from django.urls import reverse, resolve
from django.test import TestCase

from .utils import add_just_board_data


class TestUrls(TestCase):

    def setUp(self):
        add_just_board_data()

    def test_about_topic_connection(self):
        path = reverse('about')
        response = self.client.get(path)
        # self.assertContains(self.response, 'href="/"'.format('about/'))
        self.assertNotContains(response, 'href="/board/1"'.format('about/'))
