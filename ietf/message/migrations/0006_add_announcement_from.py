# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 16:10
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    AnnouncementFrom = apps.get_model('message', 'AnnouncementFrom')
    Group = apps.get_model('group', 'Group')
    RoleName = apps.get_model('name', 'RoleName')

    chair = RoleName.objects.get(slug='chair')
    admdir = RoleName.objects.get(slug='admdir')
    execdir = RoleName.objects.get(slug='execdir')
    ceo = RoleName.objects.get(slug='ceo')
    secr = RoleName.objects.get(slug='secr')

    # IETF Chair
    ietf = Group.objects.get(acronym='ietf')
    AnnouncementFrom.objects.create(name=chair,group=ietf,address='IETF Chair <chair@ietf.org>')
    AnnouncementFrom.objects.create(name=chair,group=ietf,address='The IESG <iesg@ietf.org>')

    # IAB Chair
    iab = Group.objects.get(acronym='iab')
    AnnouncementFrom.objects.create(name=chair,group=iab,address='IAB Chair <iab-chair@ietf.org>')

    # IAB Execdir
    AnnouncementFrom.objects.create(name=execdir,group=iab,address='IAB Executive Administrative Manager <execd@iab.org>')
    AnnouncementFrom.objects.create(name=execdir,group=iab,address='IAB Chair <iab-chair@ietf.org>')

    # IAD
    AnnouncementFrom.objects.create(name=admdir,group=ietf,address='IETF Administrative Director <iad@ietf.org>')
    AnnouncementFrom.objects.create(name=admdir,group=ietf,address='The IETF Trust <ietf-trust@ietf.org>')
    AnnouncementFrom.objects.create(name=admdir,group=ietf,address='ISOC CEO <ceo@isoc.org>')
    AnnouncementFrom.objects.create(name=admdir,group=ietf,address='IAOC Chair <iaoc-chair@ietf.org>')

    # RSOC Chair
    rsoc = Group.objects.get(acronym='rsoc')
    AnnouncementFrom.objects.create(name=chair,group=rsoc,address='RSOC Chair <rsoc-chair@iab.org>')

    # IAOC Chair
    iaoc = Group.objects.get(acronym='iaoc')
    AnnouncementFrom.objects.create(name=chair,group=iaoc,address='IAOC Chair <iaoc-chair@ietf.org>')

    # RSE Chair
    rse = Group.objects.get(acronym='rse')
    AnnouncementFrom.objects.create(name=chair,group=rse,address='RFC Series Editor <rse@rfc-editor.org>')

    # Mentor Chair
    mentor = Group.objects.get(acronym='mentor')
    AnnouncementFrom.objects.create(name=chair,group=mentor,address='IETF Mentoring Program <mentoring@ietf.org>')
    
    # ISOC CEO
    isoc = Group.objects.get(acronym='isoc')
    AnnouncementFrom.objects.create(name=ceo,group=isoc,address='ISOC CEO <ceo@isoc.org>')
    
    # ISOC BOARD OF TRUSTEES
    isocbot = Group.objects.get(acronym='isocbot')
    AnnouncementFrom.objects.create(name=chair,group=isocbot,address='ISOC Board of Trustees <bob.hinden@gmail.com>')
    
    # IETF TRUST
    ietftrust = Group.objects.get(acronym='ietf-trust')
    AnnouncementFrom.objects.create(name=chair,group=ietftrust,address='The IETF Trust <ietf-trust@ietf.org>')
    
    # Misc
    secretariat = Group.objects.get(acronym='secretariat')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='IETF Secretariat <ietf-secretariat@ietf.org>')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='IESG Secretary <iesg-secretary@ietf.org>')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='Internet-Drafts Administrator <internet-drafts@ietf.org>')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='IETF Agenda <agenda@ietf.org>')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='IETF Registrar <ietf-registrar@ietf.org>')
    AnnouncementFrom.objects.create(name=secr,group=secretariat,address='IETF Executive Director <exec-director@ietf.org>')

def backwards(apps, schema_editor):
    AnnouncementFrom = apps.get_model('announcement', "AnnouncementFrom")
    AnnouncementFrom.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_announcementfrom'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
