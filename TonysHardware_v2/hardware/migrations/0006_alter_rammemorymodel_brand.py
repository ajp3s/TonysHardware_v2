# Generated by Django 4.2.3 on 2023-08-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_alter_rammemorymodel_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rammemorymodel',
            name='brand',
            field=models.CharField(choices=[('Hynix', 'Hynix'), ('Patriot', 'Patriot'), ('ADATA', 'ADATA'), ('Transcend', 'Transcend'), ('G.Skill', 'G.Skill'), ('Mushkin', 'Mushkin'), ('Corsair', 'Corsair'), ('Samsung', 'Samsung'), ('Kingston', 'Kingston'), ('Team Group', 'Team Group'), ('GeIL', 'GeIL'), ('Apacer', 'Apacer'), ('Micron', 'Micron'), ('PNY', 'PNY'), ('Crucial', 'Crucial'), ('Smart Modular', 'Smart Modular'), ('Qimonda', 'Qimonda')], max_length=50),
        ),
    ]
