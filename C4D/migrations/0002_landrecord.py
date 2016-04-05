# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C4D', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grantor', models.CharField(max_length=64)),
                ('grantee', models.CharField(max_length=64)),
            ],
        ),
    ]
