# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180107_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('note', models.TextField(blank=True, null=True)),
                ('createtime', models.DateField(auto_now_add=True, null=True)),
                ('updatetime', models.DateField(auto_now=True, null=True)),
                ('city', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='pulish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Publish'),
        ),
    ]
