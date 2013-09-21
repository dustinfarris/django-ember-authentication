from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.serializers import UserSerializer


class CreateUserTest(APITestCase):
    def setUp(self):
        self.data = {'username': 'fred', 'first_name': 'Fred', 'last_name': 'Willums'}

    def test_can_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="jake")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="jake", first_name="Jake")
        self.data = UserSerializer(self.user).data
        self.data.update({'first_name': 'Changed'})

    def test_can_update_user(self):
        response = self.client.put(reverse('user-detail', args=[self.user.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="jake")

    def test_can_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
