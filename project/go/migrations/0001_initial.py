# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GoGame'
        db.create_table(u'go_gogame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sgf_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'go', ['GoGame'])


    def backwards(self, orm):
        # Deleting model 'GoGame'
        db.delete_table(u'go_gogame')


    models = {
        u'go.gogame': {
            'Meta': {'object_name': 'GoGame'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sgf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['go']