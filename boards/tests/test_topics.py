from django.urls import reverse, resolve
from django.test import TestCase

from .utils import add_data


class TestUrls(TestCase):

    def setUp(self):
        add_data()

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

    def test_board_topics_new_topic_button(self):
        path = reverse('board_topics', args=[1])
        response = self.client.get(path)
        self.assertContains(response, 'href="/board/1/new/"'.format(path))

    def test_board_topics_new_topic_button_fail(self):
        path = reverse('board_topics', args=[2])
        response = self.client.get(path)
        self.assertNotContains(response, 'href="/board/1/new/"'.format(path))

    def test_board_topics_list(self):
        path = reverse('board_topics', args=[1])
        response = self.client.get(path)
        self.assertContains(response, '<td>test1</td>'.format(path))
        self.assertContains(response, '<td>test</td>'.format(path))
