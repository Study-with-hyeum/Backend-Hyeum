from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_can_create_a_user(self):
        email = 'test@test.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))
