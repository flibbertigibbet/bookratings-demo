from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from http.cookies import SimpleCookie

from ratings.forms import DUMMY_PASSWORD
from ratings.views import USERNAME_COOKIE


UserModel = get_user_model()


class IndexViewTextCase(TestCase):
    def setUp(self):
        self.client = Client()
        user_name = 'existinguser'
        # create a user
        self.user = UserModel.objects.create(username=user_name)
        self.user.set_password(DUMMY_PASSWORD)
        self.user.save()

    def test_index_page_redirects_when_no_cookie(self):
        """Should redirect to sign-up page if not signed in and username cookie not set"""
        response = self.client.get('')
        self.assertRedirects(
            response, '/signup/', status_code=302, target_status_code=200)

    def test_index_page_creates_user_from_cookie(self):
        """Should create user from user name in cookie if user doesn't already exist.

        Check user creation from name in cookie where user not signed in yet and does not yet exist.
        """
        user_name = 'testuser'
        self.client.cookies = SimpleCookie({USERNAME_COOKIE: user_name})
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, user_name)

    def test_index_page_logs_in_user_from_cookie(self):
        """Should log in user from user name in cookie if user with that name already exists.

        Check user sign-in from name in cookie where user not signed in yet but does exist.
        """
        self.client.cookies = SimpleCookie({USERNAME_COOKIE: self.user.username})
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, self.user.username)

    def test_index_page_creates_cookie_for_user(self):
        """If user is authenticated but the username cookie isn't present, set it."""
        self.client.login(username=self.user.username, password=DUMMY_PASSWORD)
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.cookies.get('username').value, self.user.username)
