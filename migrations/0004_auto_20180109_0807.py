# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180109_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pulish',
            new_name='publish',
        ),
    ]