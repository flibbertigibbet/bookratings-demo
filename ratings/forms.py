from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UsernameField

from .models import Book, UserRating


DUMMY_PASSWORD = 'blank'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'isbn')


class RatingsForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ('user', 'book', 'stars', 'rating')


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
