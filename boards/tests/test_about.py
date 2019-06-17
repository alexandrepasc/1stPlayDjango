from django.urls import reverse, resolve
from django.test import TestCase

from .utils import add_just_board_data


class TestUrls(TestCase):
    path = reverse('about')

    def setUp(self):
        add_just_board_data()

    def test_about_topic_connection(self):
        response = self.client.get(self.path)
        # self.assertContains(self.response, 'href="/"'.format('about/'))
        self.assertNotContains(response, 'href="/board/1"'.format('about/'))

    def test_signup_button(self):
        signup = reverse('signup')
        response = self.client.get(self.path)
        self.assertContains(response, 'href="' + signup + '"'.format(self.path))
