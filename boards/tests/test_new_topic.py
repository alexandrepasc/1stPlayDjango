from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board, Post, Topic, User
from .utils import add_data


class TestNewTopic(TestCase):
    path = reverse('new_topic', args=[1])

    def setUp(self):
        add_data()

    def test_new_topic_url(self):
        assert resolve(self.path).view_name == 'new_topic'

    def test_new_topic_status(self):
        response = self.client.get(self.path)
        assert response.status_code == 200

    def test_new_topic_status_fail(self):
        path = reverse('new_topic', args=[99])
        response = self.client.get(path)
        assert response.status_code == 404

    def test_new_topic_cancel(self):
        response = self.client.get(self.path)
        self.assertContains(response, 'formaction="/board/1/"'.format(self.path))

    def test_new_topic_cancel_fail(self):
        path = reverse('new_topic', args=[2])
        response = self.client.get(path)
        self.assertNotContains(response, 'formaction="/board/1/"'.format(path))

    def test_csrf(self):
        response = self.client.get(self.path)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic(self):
        data = {
            'subject': 'title',
            'message': 'description'
        }
        response = self.client.post(self.path, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_fail(self):
        response = self.client.post(self.path, {})
        self.assertEquals(response.status_code, 200)

    def test_signup_button(self):
        signup = reverse('signup')
        response = self.client.get(self.path)
        self.assertContains(response, 'href="' + signup + '"'.format(self.path))
