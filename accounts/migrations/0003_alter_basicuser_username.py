# Generated by Django 4.2.3 on 2023-07-29 14:39

import TonysHardware_v2.validators.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_basicuser_additional_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[TonysHardware_v2.validators.custom_validators.letters_numbers_and_underscores_validator]),
        ),
    ]