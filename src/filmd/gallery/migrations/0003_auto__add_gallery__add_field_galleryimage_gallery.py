# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('gallery', ['Gallery'])

        # Adding field 'GalleryImage.gallery'
        db.add_column('gallery_galleryimage', 'gallery',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Gallery']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')

        # Deleting field 'GalleryImage.gallery'
        db.delete_column('gallery_galleryimage', 'gallery_id')


    models = {
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'gallery.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']