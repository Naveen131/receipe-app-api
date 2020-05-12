from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@gmail.com"
        password = "Testpass123"
        user  = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    def test_new_user_email_normalized(self):
        email = "tets@GMAIL.COM"
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
       with self.assertRaises(ValueError):
           user = get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        email = "test@gmail.com"
        password = "Testpass123"
        user  = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
