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

    def test_form_no_input_url(self):
        response = self.client.post(self.path, {})
        assert resolve(self.path).view_name == 'signup'

    def test_form_no_input_status(self):
        response = self.client.post(self.path, {})
        assert response.status_code == 200

    def test_form_errors(self):
        response = self.client.post(self.path, {})
        form = response.context.get('form')
        self.assertTrue(form.errors)

    # def test_form_with_input_url(self):
    #     data = {
    #         'username': 'test',
    #         'email': 'test@mail.com',
    #         'password1': 'abcdef123456',
    #         'password2': 'abcdef123456'
    #     }
    #     response = self.client.post(self.path, data)
    #     form = response.context.get('form')
    #     print(form.errors)
    #     assert resolve(self.path).view_name == 'home'

    # def test_user_authentication(self):
    #     data = {
    #             'username': 'test',
    #             'email': 'test@mail.com',
    #             'password1': 'abcdef123456',
    #             'password2': 'abcdef123456'
    #     }
    #     response = self.client.post(self.path, data)
    #     user = response.context.get('user')
    #     self.assertTrue(user.is_authenticated)
