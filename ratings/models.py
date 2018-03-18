from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False, default='')
    isbn = models.CharField(max_length=128, blank=False, null=False, unique=True)
    added_by = models.ForeignKey(User, null=False, blank=True)

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
    #    super(Book, self).save(*args, **kwargs)


class UserRating(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    book = models.ForeignKey('Book', null=False, blank=False)
    stars = models.PositiveSmallIntegerField()
    rating = models.TextField()

    def validate_unique(self, exclude=None, *args, **kwargs):
        super(UserRating, self).validate_unique(*args, **kwargs)
        ratings = UserRating.objects.filter(user=self.user)
        if ratings.filter(book=self.book).exists():
            raise ValidationError("User may only have one rating per book.")

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(UserRating, self).save(*args, **kwargs)
