from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
# Create your tests here.


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')


def test_user_registration_get(self):
    response = self.client.get(self.path)

    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertEqual(response.context_data['title'], 'Store - Регистрация')
