from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class SessionViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="bob",
            first_name="Bob",
            last_name="Barker")
        self.user.set_password("correct")
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_get_session_with_active_session(self):
        """
        Should return a hash containing the current user's id.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/session/')
        expected = {'user_id': self.user.id}
        self.assertEqual(response.data, expected)

    def test_get_session_with_no_active_session(self):
        """
        Should return a hash with `user_id` set to None.
        """
        response = self.client.get('/session/')
        expected = {'user_id': None}
        self.assertEqual(response.data, expected)

    def test_create_session_with_valid_credentials(self):
        """
        Should log the user in and return a JSON object with a success
        flag and the user's id.
        """
        data = {'username': 'bob', 'password': 'correct'}
        response = self.client.post('/session/', data)
        expected = {'success': True, 'user_id': self.user.id}
        self.assertEqual(response.data, expected)
        self.assertEqual(self.client.session['_auth_user_id'], self.user.id)

    def test_create_session_with_invalid_credentials(self):
        """
        Should not log the user in and return a JSON object with a
        failing success flag and error message.
        """
        data = {'username': 'bob', 'password': 'wrong'}
        response = self.client.post('/session/', data)
        expected = {'success': False, 'user_id': None, 'message': 'Invalid username or password'}
        self.assertEqual(response.data, expected)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_create_session_when_user_is_not_active(self):
        """
        Should not log the user in and return a JSON object with a
        failing success flag and error message.
        """
        self.user.is_active = False
        self.user.save()
        data = {'username': 'bob', 'password': 'correct'}
        response = self.client.post('/session/', data)
        expected = {'success': False, 'user_id': None, 'message': 'Sorry, this account is suspended'}
        self.assertEqual(response.data, expected)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_destroy_session(self):
        """
        Should log the user out and return an empty response.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete('/session/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn('_auth_user_id', self.client.session)
