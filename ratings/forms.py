from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UsernameField

from .models import Book, UserRating


UserModel = get_user_model()
DUMMY_PASSWORD = 'blank'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'isbn')


class RatingsForm(forms.ModelForm):
    class Meta:
        model = UserRating
        # TODO:


class RatingsUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username.

    Assigns a default password (this demo app has no authentication).
    """

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {UserModel.USERNAME_FIELD: UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(DUMMY_PASSWORD)
        if commit:
            user.save()
        return user
