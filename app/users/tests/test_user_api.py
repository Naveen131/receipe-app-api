from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**param):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):

    def setUp(self):
        set.client = APIClient()

    def test_create_user_success(self):
        payload = {
            "email":"test@gmail.com",
            "password":"123456",
            "name":"Test Name"
        }

        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,ststus.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)


    def test_user_exits(self):
        payload = {
            "email":"test@gmail.com",
            "password":"123456",
            "name":"Test Name"
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "email":"test@gmail.com",
            "password":"too",
            "name":"Test Name"
        }

        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']

        ).exists()
        self.assertFalse(user_exists)
