# Generated by Django 3.0.7 on 2020-06-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_aporteparafiscal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aporteparafiscal',
            options={'verbose_name': 'Aporte Parafiscal', 'verbose_name_plural': 'Aportes Parafiscales'},
        ),
        migrations.AlterField(
            model_name='idioma',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]