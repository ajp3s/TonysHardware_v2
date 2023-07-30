# Generated by Django 4.2.3 on 2023-07-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_alter_rammemory_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMDRadeonGPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(choices=[('Radeon RX', ' Radeon RX'), ('Radeon R9', 'Radeon R9'), ('Radeon R8', 'Radeon R8'), ('Radeon R7', 'Radeon R7'), ('Radeon R6', 'Radeon R6'), ('Radeon R5', 'Radeon R5'), ('Radeon R4', 'Radeon R4'), ('Radeon R3', 'Radeon R3'), ('Radeon R2', 'Radeon R2')], max_length=20)),
                ('type', models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop', 'Laptop'), ('Integrated(iGPU)', 'Integrated(iGPU)')], max_length=20)),
                ('series', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('graphics_processor', models.CharField(max_length=20)),
                ('architecture', models.CharField(max_length=20)),
                ('process_size', models.CharField(max_length=5)),
                ('transistors_count', models.CharField(max_length=30)),
                ('base_clock', models.PositiveIntegerField()),
                ('boost_clock', models.PositiveIntegerField()),
                ('memory_clock', models.PositiveIntegerField()),
                ('memory_bus_width', models.PositiveIntegerField()),
                ('memory_bandwidth', models.PositiveIntegerField()),
                ('release_date', models.DateField(auto_now=True)),
                ('tdp', models.PositiveIntegerField(verbose_name='Thermal Design Power(TDP)')),
                ('suggested_psu', models.CharField(max_length=10)),
                ('graphics_api_support', models.CharField(max_length=60)),
                ('amd_radeon_gpu_image', models.ImageField(upload_to='nvidia_gpu_images/')),
                ('maximum_gpu_temperature', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='nvidiagpu',
            old_name='bandwidth',
            new_name='memory_bandwidth',
        ),
        migrations.RenameField(
            model_name='nvidiagpu',
            old_name='transistors',
            new_name='transistors_count',
        ),
        migrations.AddField(
            model_name='nvidiagpu',
            name='generation',
            field=models.CharField(choices=[('Nvidia GeForce RTX', 'Nvidia GeForce RTX'), ('Nvidia GeForce GTX', 'Nvidia GeForce GTX'), ('Nvidia RTX', 'Nvidia RTX'), ('Nvidia T', 'Nvidia T'), ('Nvidia L', 'Nvidia L')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='nvidiagpu',
            name='maximum_gpu_temperature',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='nvidiagpu',
            name='type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop', 'Laptop')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rammemory',
            name='brand',
            field=models.CharField(choices=[('Kingston', 'Kingston'), ('GeIL', 'GeIL'), ('Mushkin', 'Mushkin'), ('Corsair', 'Corsair'), ('Crucial', 'Crucial'), ('Samsung', 'Samsung'), ('Transcend', 'Transcend'), ('Hynix', 'Hynix'), ('PNY', 'PNY'), ('Qimonda', 'Qimonda'), ('G.Skill', 'G.Skill'), ('ADATA', 'ADATA'), ('Smart Modular', 'Smart Modular'), ('Patriot', 'Patriot'), ('Micron', 'Micron'), ('Apacer', 'Apacer'), ('Team Group', 'Team Group')], max_length=50),
        ),
    ]
