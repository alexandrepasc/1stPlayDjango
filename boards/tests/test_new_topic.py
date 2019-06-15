from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board


class TestNewTopic(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        Board.objects.create(name='Python', description='Python board.')

    def test_new_topic_url(self):
        path = reverse('new_topic', args=[1])
        assert resolve(path).view_name == 'new_topic'

    def test_new_topic_status(self):
        path = reverse('new_topic', args=[1])
        response = self.client.get(path)
        assert response.status_code == 200

    def test_new_topic_status_fail(self):
        path = reverse('new_topic', args=[99])
        response = self.client.get(path)
        assert response.status_code == 404

    def test_new_topic_cancel(self):
        path = reverse('new_topic', args=[1])
        response = self.client.get(path)
        self.assertContains(response, 'href="/board/1"'.format('new_topic/'))

    def test_new_topic_cancel_fail(self):
        path = reverse('new_topic', args=[2])
        response = self.client.get(path)
        self.assertNotContains(response, 'href="/board/1"'.format('new_topic/'))
