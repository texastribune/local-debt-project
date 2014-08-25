# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CityDebt'
        db.create_table(u'debt_context_citydebt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('govt_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('debt_principal_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('debt_interest_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('debt_service_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('m_and_o_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('i_and_s_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('total_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_year_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('tax_debt_to_assessed_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_debt_service_to_av', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_debt_per_capita', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'debt_context', ['CityDebt'])

        # Adding model 'CountyDebt'
        db.create_table(u'debt_context_countydebt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('govt_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('debt_principal_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('debt_interest_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('debt_service_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('m_and_o_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('i_and_s_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('total_tax_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_year_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('tax_debt_to_assessed_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_debt_service_to_av', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('tax_debt_per_capita', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'debt_context', ['CountyDebt'])

        # Adding model 'SchoolDistrictDebt'
        db.create_table(u'debt_context_schooldistrictdebt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('govt_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('issuer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tax_year_assessed_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('full_year_ada_2012', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('voter_approved_debt_principal_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('voter_approved_debt_interest_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('voter_approved_debt_service_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('m_and_o_debt_principal_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('m_and_o_debt_interest_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('m_and_o_debt_service_outstanding', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('total_debt_per_student', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('total_debt_per_assessed_valuation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('combined_principal_debt', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'debt_context', ['SchoolDistrictDebt'])


    def backwards(self, orm):
        # Deleting model 'CityDebt'
        db.delete_table(u'debt_context_citydebt')

        # Deleting model 'CountyDebt'
        db.delete_table(u'debt_context_countydebt')

        # Deleting model 'SchoolDistrictDebt'
        db.delete_table(u'debt_context_schooldistrictdebt')


    models = {
        u'debt_context.citydebt': {
            'Meta': {'object_name': 'CityDebt'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'debt_interest_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'debt_principal_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'debt_service_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'i_and_s_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'm_and_o_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tax_debt_per_capita': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_debt_service_to_av': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_debt_to_assessed_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_year_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'total_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'debt_context.countydebt': {
            'Meta': {'object_name': 'CountyDebt'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'debt_interest_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'debt_principal_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'debt_service_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'govt_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'i_and_s_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'm_and_o_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tax_debt_per_capita': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_debt_service_to_av': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_debt_to_assessed_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_year_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'total_tax_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'debt_context.schooldistrictdebt': {
            'Meta': {'object_name': 'SchoolDistrictDebt'},
            'combined_principal_debt': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'full_year_ada_2012': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'govt_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'm_and_o_debt_interest_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'm_and_o_debt_principal_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'm_and_o_debt_service_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'tax_year_assessed_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'total_debt_per_assessed_valuation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'total_debt_per_student': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'voter_approved_debt_interest_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'voter_approved_debt_principal_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'voter_approved_debt_service_outstanding': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['debt_context']