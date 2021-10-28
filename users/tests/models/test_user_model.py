from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    def test_create_user_successful(self):
        """Test creating a new user"""
        email = 'test@email.com'
        password = 'password1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))
