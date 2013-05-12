# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')

        # Deleting field 'GalleryImage.gallery'
        db.delete_column('gallery_galleryimage', 'gallery_id')


    def backwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal('gallery', ['Gallery'])


        # User chose to not deal with backwards NULL issues for 'GalleryImage.gallery'
        raise RuntimeError("Cannot reverse this migration. 'GalleryImage.gallery' and its values cannot be restored.")

    models = {
        'gallery.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']