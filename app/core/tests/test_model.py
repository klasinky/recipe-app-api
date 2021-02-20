from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating  a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email, "User's email is not the same")
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """

        email = 'test@TeST.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='Password12Test34'
        )

        self.assertEqual(user.email, email.lower(), 'Email is not normalized')

    def test_new_user_email_invalid(self):
        """Test creating user with no email raises error """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='pepito'
            )

    def test_create_new_superuser(self):
        """ Test creating a new superuser """

        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='PasswordTest123'
        )

        self.assertTrue(user.is_superuser, 'User is not superuser')
        self.assertTrue(user.is_staff, 'User is not staff')
