from django.urls import reverse, resolve
from django.test import TestCase


class TestUrls(TestCase):

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_home_status(self):
        path = reverse('home')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_signup_button(self):
        path = reverse('home')
        signup = reverse('signup')
        response = self.client.get(path)
        self.assertContains(response, 'href="' + signup + '"'.format(path))
