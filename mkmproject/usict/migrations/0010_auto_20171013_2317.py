# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usict', '0009_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
