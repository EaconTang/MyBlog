# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0020_auto_20160723_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibo',
            name='wb_pub_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=b'Publish Time'),
        ),
    ]