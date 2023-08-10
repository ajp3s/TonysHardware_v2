# Generated by Django 4.2.3 on 2023-08-10 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_articlemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='content',
            field=models.TextField(max_length=15000),
        ),
    ]