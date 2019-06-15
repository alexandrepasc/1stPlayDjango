from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board


class TestUrls(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        Board.objects.create(name='Python', description='Python board.')

    def test_board_topics_url(self):
        path = reverse('board_topics', args=[1])
        assert resolve(path).view_name == 'board_topics'

    def test_board_topics_status(self):
        path = reverse('board_topics', args=[1])
        response = self.client.get(path)
        assert response.status_code == 200

    def test_board_topics_status_fail(self):
        path = reverse('board_topics', args=[99])
        response = self.client.get(path)
        assert response.status_code == 404