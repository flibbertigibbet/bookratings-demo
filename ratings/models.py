from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False, default='')
    isbn = models.CharField(max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return self.title
