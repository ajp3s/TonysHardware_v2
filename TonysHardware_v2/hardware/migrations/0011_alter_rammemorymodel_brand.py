# Generated by Django 4.2.3 on 2023-08-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0010_remove_motherboardmodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rammemorymodel',
            name='brand',
            field=models.CharField(choices=[('G.Skill', 'G.Skill'), ('Crucial', 'Crucial'), ('Mushkin', 'Mushkin'), ('Transcend', 'Transcend'), ('Patriot', 'Patriot'), ('Apacer', 'Apacer'), ('PNY', 'PNY'), ('GeIL', 'GeIL'), ('Qimonda', 'Qimonda'), ('Smart Modular', 'Smart Modular'), ('Kingston', 'Kingston'), ('Corsair', 'Corsair'), ('ADATA', 'ADATA'), ('Micron', 'Micron'), ('Team Group', 'Team Group'), ('Hynix', 'Hynix'), ('Samsung', 'Samsung')], max_length=50),
        ),
    ]
