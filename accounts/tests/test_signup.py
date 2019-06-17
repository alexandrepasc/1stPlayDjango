from django.urls import reverse, resolve
from django.test import TestCase


class TestSignUp(TestCase):
    path = reverse('signup')

    def test_url(self):
        assert resolve(self.path).view_name == 'signup'

    def test_status(self):
        response = self.client.get(self.path)
        assert response.status_code == 200

    def test_home_button(self):
        home = reverse('home')
        response = self.client.get(self.path)
        self.assertContains(response, 'href="' + home + '"'.format(self.path))

    def test_about_button(self):
        about = reverse('about')
        response = self.client.get(self.path)
        self.assertContains(response, 'href="' + about + '"'.format(self.path))

    def test_signup_button(self):
        response = self.client.get(self.path)
        self.assertNotContains(response, 'href="' + self.path + '"'.format(self.path))
