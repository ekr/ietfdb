# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-06 03:42
from __future__ import unicode_literals

from django.db import migrations

def forwards(apps,schema_editor):
    DraftSubmissionStateName = apps.get_model('name','DraftSubmissionStateName')

    auth      = DraftSubmissionStateName.objects.get(slug='auth')
    aut_appr  = DraftSubmissionStateName.objects.get(slug='aut-appr')
    cancelled = DraftSubmissionStateName.objects.get(slug='cancel')
    posted    = DraftSubmissionStateName.objects.get(slug='posted')

    confirmed = DraftSubmissionStateName.objects.create(
        slug = 'confirmed',
        name = 'Confirmed',
        )

    confirmed.next_states.add(cancelled, posted)
    auth.next_states.add(confirmed)
    aut_appr.next_states.add(confirmed)

def backwards(apps,schema_editor):
    DraftSubmissionStateName = apps.get_model('name','DraftSubmissionStateName')

    auth      = DraftSubmissionStateName.objects.get(slug='auth')
    aut_appr  = DraftSubmissionStateName.objects.get(slug='aut-appr')
    confirmed = DraftSubmissionStateName.objects.get(slug='confirmed')

    auth.next_states.remove(confirmed)
    aut_appr.next_states.remove(confirmed)

    confirmed.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0028_add_docurltagname_entries'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
