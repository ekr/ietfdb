# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-07 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_registration_registrationstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingregistration',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
