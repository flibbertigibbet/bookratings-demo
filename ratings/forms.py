from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField

from .models import Book, BookRating


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

    stars = forms.ChoiceField(widget=forms.RadioSelect, choices=((x, x) for x in range(1, 6)))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RateBookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BookRating
        fields = ('book', 'stars', 'rating')

    def clean(self):
        self.instance.user = self.user
        return super(RateBookForm, self).clean()

    def save(self, commit=True):
        self.instance.user = self.user
        rating = super().save(commit=False)
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
