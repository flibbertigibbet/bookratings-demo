# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_book_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=128, unique=True, verbose_name='ISBN'),
        ),
    ]
