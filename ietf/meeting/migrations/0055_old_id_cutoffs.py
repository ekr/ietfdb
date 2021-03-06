# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 01:35
from __future__ import unicode_literals

from django.db import migrations
import datetime

def forward(apps, schema_editor):
    ImportantDate = apps.get_model('meeting','ImportantDate')
    Meeting = apps.get_model('meeting','Meeting')
    for m in Meeting.objects.filter(type='ietf').exclude(importantdate__isnull=False):
        if m.idsubmit_cutoff_day_offset_00 == m.idsubmit_cutoff_day_offset_01 :
            ImportantDate.objects.create(
                name_id='idcutoff',
                meeting=m,
                date=m.date-datetime.timedelta(days=m.idsubmit_cutoff_day_offset_00) 
            )
        else:
            ImportantDate.objects.create(
                name_id='00cutoff',
                meeting=m,
                date=m.date-datetime.timedelta(days=m.idsubmit_cutoff_day_offset_00) 
            )
            ImportantDate.objects.create(
                name_id='01cutoff',
                meeting=m,
                date=m.date-datetime.timedelta(days=m.idsubmit_cutoff_day_offset_01) 
            )
        
 
def reverse(apps, schema_editor):
    Meeting = apps.get_model('meeting','Meeting')
    # This is a simple reverse implementation. If a reverse is needed a significant
    # time after the forward is run (as in multiple meeting cycles), a more considered
    # implemenation should be created reflecting any assumptions that have changed in
    # that time.
    for m in Meeting.objects.filter(type='ietf'):
        if m.importantdate_set.count()==2:
            m.importantdate_set.all().delete()
        
class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0054_earlier_important_dates'),
    ]

    operations = [
        migrations.RunPython(forward,reverse)
    ]
