# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RoomResourceName'
        db.create_table('name_roomresourcename', (
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('name', ['RoomResourceName'])

    def backwards(self, orm):
        # Deleting model 'RoomResourceName'
        db.delete_table('name_roomresourcename')


    models = {
        'name.ballotpositionname': {
            'Meta': {'ordering': "['order']", 'object_name': 'BallotPositionName'},
            'blocking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.constraintname': {
            'Meta': {'ordering': "['order']", 'object_name': 'ConstraintName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'penalty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.dbtemplatetypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'DBTemplateTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.docrelationshipname': {
            'Meta': {'ordering': "['order']", 'object_name': 'DocRelationshipName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'revname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.docremindertypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'DocReminderTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.doctagname': {
            'Meta': {'ordering': "['order']", 'object_name': 'DocTagName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.doctypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'DocTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.feedbacktype': {
            'Meta': {'ordering': "['order']", 'object_name': 'FeedbackType'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.groupmilestonestatename': {
            'Meta': {'ordering': "['order']", 'object_name': 'GroupMilestoneStateName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.groupstatename': {
            'Meta': {'ordering': "['order']", 'object_name': 'GroupStateName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.grouptypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'GroupTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.intendedstdlevelname': {
            'Meta': {'ordering': "['order']", 'object_name': 'IntendedStdLevelName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.liaisonstatementpurposename': {
            'Meta': {'ordering': "['order']", 'object_name': 'LiaisonStatementPurposeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.meetingtypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'MeetingTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.nomineepositionstate': {
            'Meta': {'ordering': "['order']", 'object_name': 'NomineePositionState'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.rolename': {
            'Meta': {'ordering': "['order']", 'object_name': 'RoleName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.roomresourcename': {
            'Meta': {'ordering': "['order']", 'object_name': 'RoomResourceName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.sessionstatusname': {
            'Meta': {'ordering': "['order']", 'object_name': 'SessionStatusName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.stdlevelname': {
            'Meta': {'ordering': "['order']", 'object_name': 'StdLevelName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.streamname': {
            'Meta': {'ordering': "['order']", 'object_name': 'StreamName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'name.timeslottypename': {
            'Meta': {'ordering': "['order']", 'object_name': 'TimeSlotTypeName'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['name']