# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rep_api', '0002_rep_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rep',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='rep',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
