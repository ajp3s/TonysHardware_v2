# Generated by Django 4.2.3 on 2023-07-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_imagegallerymodel_delete_galleryimage_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='imagegallerymodel',
            name='user_gallery_limit',
        ),
    ]
