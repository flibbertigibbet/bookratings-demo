from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False, default='')
    isbn = models.CharField(max_length=128, blank=False, null=False, unique=True,
                            verbose_name="ISBN")
    added_by = models.ForeignKey(User, null=False, blank=True)

    def __str__(self):
        return self.title


class BookRating(models.Model):
    user = models.ForeignKey(User, null=False, blank=True)
    book = models.ForeignKey('Book', null=False, blank=False)
    stars = models.PositiveSmallIntegerField()
    rating = models.TextField()

    def validate_unique(self, exclude=None, *args, **kwargs):
        super(BookRating, self).validate_unique(*args, **kwargs)
        ratings = BookRating.objects.filter(user=self.user)
        if ratings.filter(book=self.book).exists():
            raise ValidationError("User may only have one rating per book.")

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(BookRating, self).save(*args, **kwargs)
