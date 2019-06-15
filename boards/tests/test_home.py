from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board


class TestUrls(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        Board.objects.create(name='Python', description='Python board.')


    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'


    def test_home_status(self):
        path = reverse('home')
        response = self.client.get(path)
        assert response.status_code == 200