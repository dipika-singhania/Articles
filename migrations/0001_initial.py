# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=40)),
                ('publication_date', models.DateField()),
                ('hero_image', models.ImageField(upload_to='hero_images/')),
                ('additional_image', models.ImageField(upload_to='addtional_images/')),
                ('article_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_choice', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.Category'),
        ),
    ]
