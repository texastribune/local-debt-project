# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collection'
        db.create_table(u'boundaries_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('authority', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_updated', self.gf('django.db.models.fields.DateField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal(u'boundaries', ['Collection'])

        # Adding model 'Shape'
        db.create_table(u'boundaries_shape', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shapes', null=True, to=orm['boundaries.Collection'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('identifier', self.gf('django.db.models.fields.IntegerField')()),
            ('shape', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'boundaries', ['Shape'])


    def backwards(self, orm):
        # Deleting model 'Collection'
        db.delete_table(u'boundaries_collection')

        # Deleting model 'Shape'
        db.delete_table(u'boundaries_shape')


    models = {
        u'boundaries.collection': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Collection'},
            'authority': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        u'boundaries.shape': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Shape'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shapes'", 'null': 'True', 'to': u"orm['boundaries.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shape': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['boundaries']