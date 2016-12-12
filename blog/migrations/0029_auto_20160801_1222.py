# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20160726_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mdfile',
            name='md_modified',
        ),
        migrations.AddField(
            model_name='mdfile',
            name='md_catalogue',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mdfile',
            name='md_visit',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Visits'),
        ),
    ]