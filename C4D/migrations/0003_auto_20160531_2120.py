# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C4D', '0002_rawlandrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawlandrecord',
            name='grantee',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='rawlandrecord',
            name='grantor',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]