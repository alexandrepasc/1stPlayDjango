from django.urls import reverse, resolve
from django.test import TestCase


class TestUrls(TestCase):
    path = reverse('home')

    def test_home_url(self):
        assert resolve(self.path).view_name == 'home'

    def test_home_status(self):
        response = self.client.get(self.path)
        assert response.status_code == 200

    def test_signup_button(self):
        signup = reverse('signup')
        response = self.client.get(self.path)
        self.assertContains(response, 'href="' + signup + '"'.format(self.path))
