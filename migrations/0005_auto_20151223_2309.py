# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_auto_20151219_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
