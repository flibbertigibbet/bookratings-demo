from django.contrib.auth.models import User
from django.test import TestCase

from ratings.forms import AddBookForm, RatingsUserCreationForm
from ratings.models import Book


class AddBookFormTestCase(TestCase):
    def setUp(self):
        user_name = 'user'
        self.user = User.objects.create(username=user_name)

    def test_add_book(self):
        form_data = {'title': 'title', 'isbn': '1111'}
        form = AddBookForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEquals(Book.objects.filter(isbn=form_data['isbn']).count(), 1)

    def test_cannot_add_book_with_existing_isbn(self):
        # add first book
        form_data = {'title': 'title', 'isbn': '1111'}
        form = AddBookForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())
        form.save()

        # attempt to add second book with same ISBN
        form_data['title'] = 'sequel'
        form = AddBookForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())


class UserCreationFormTestCase(TestCase):
    def test_forms(self):
        form_data = {'username': 'anything'}
        form = RatingsUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEquals(User.objects.filter(username=form_data['username']).count(), 1)
