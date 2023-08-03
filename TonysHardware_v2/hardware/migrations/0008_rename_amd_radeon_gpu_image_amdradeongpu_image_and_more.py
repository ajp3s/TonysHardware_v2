# Generated by Django 4.2.3 on 2023-08-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0007_psu_efficiency_standard_rammemory_capacity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amdradeongpu',
            old_name='amd_radeon_gpu_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='cpu_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='nvidiagpu',
            old_name='nvidia_gpu_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='psu',
            old_name='psu_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='rammemory',
            old_name='ram_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='storagedrive',
            old_name='drive_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='rammemory',
            name='brand',
            field=models.CharField(choices=[('Patriot', 'Patriot'), ('Samsung', 'Samsung'), ('Apacer', 'Apacer'), ('PNY', 'PNY'), ('G.Skill', 'G.Skill'), ('Qimonda', 'Qimonda'), ('Hynix', 'Hynix'), ('Team Group', 'Team Group'), ('Kingston', 'Kingston'), ('Corsair', 'Corsair'), ('ADATA', 'ADATA'), ('Smart Modular', 'Smart Modular'), ('Micron', 'Micron'), ('Crucial', 'Crucial'), ('Transcend', 'Transcend'), ('GeIL', 'GeIL'), ('Mushkin', 'Mushkin')], max_length=50),
        ),
    ]
