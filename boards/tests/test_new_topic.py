from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board, Post, Topic, User
from .utils import add_data


class TestNewTopic(TestCase):

    def setUp(self):
        add_data()

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
        self.assertContains(response, 'formaction="/board/1"'.format(path))

    def test_new_topic_cancel_fail(self):
        path = reverse('new_topic', args=[2])
        response = self.client.get(path)
        self.assertNotContains(response, 'formaction="/board/1"'.format(path))

    def test_csrf(self):
        path = reverse('new_topic', args=[1])
        response = self.client.get(path)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic(self):
        path = reverse('new_topic', args=[1])
        data = {
            'subject': 'title',
            'message': 'description'
        }
        response = self.client.post(path, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_fail(self):
        path = reverse('new_topic', args=[1])
        response = self.client.post(path, {})
        self.assertEquals(response.status_code, 200)
