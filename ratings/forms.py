from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError

from .models import Book, UserRating


DUMMY_PASSWORD = 'blank'


class AddBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddBookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ('title', 'isbn')

    def save(self, commit=True):
        book = super().save(commit=False)
        book.added_by = self.user
        if commit:
            book.save()
        return book


class RateBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RateBookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserRating
        fields = ('book', 'stars', 'rating')

    def clean(self):
        try:
            self.instance.validate_unique()
        except Exception as ex:
            raise ValidationError("You have already rated that book.")

    def save(self, commit=True):
        rating = super().save(commit=False)
        rating.user = self.user
        if commit:
            rating.save()
        return rating


class RatingsUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username.

    Assigns a default password (this demo app has no authentication).
    """

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)
        field_classes = {User.USERNAME_FIELD: UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(DUMMY_PASSWORD)
        if commit:
            user.save()
        return user
